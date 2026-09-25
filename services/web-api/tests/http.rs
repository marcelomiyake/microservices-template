use axum::{
    Json, Router,
    body::to_bytes,
    http::{Request, StatusCode},
    routing::get,
};
use tower::ServiceExt;
use web_api::{AppState, app};

#[derive(serde::Serialize)]
struct TestResponse {
    message: &'static str,
}

async fn response_from_upstream(upstream: Router) -> (StatusCode, String) {
    let listener = tokio::net::TcpListener::bind("127.0.0.1:0").await.unwrap();
    let address = listener.local_addr().unwrap();
    tokio::spawn(async move { axum::serve(listener, upstream).await.unwrap() });
    let state = AppState {
        client: reqwest::Client::new(),
        example_service_url: format!("http://{address}"),
    };
    let response = app(state)
        .oneshot(
            Request::builder()
                .uri("/api/example")
                .body(axum::body::Body::empty())
                .unwrap(),
        )
        .await
        .unwrap();
    let status = response.status();
    let bytes = to_bytes(response.into_body(), 1024).await.unwrap();
    (status, String::from_utf8(bytes.to_vec()).unwrap())
}

#[tokio::test]
async fn passes_through_the_owned_message() {
    let upstream = Router::new().route(
        "/example",
        get(|| async { Json(TestResponse { message: "hello" }) }),
    );
    let (status, body) = response_from_upstream(upstream).await;
    assert_eq!(status, StatusCode::OK);
    assert_eq!(body, r#"{"message":"hello"}"#);
}

#[tokio::test]
async fn translates_a_downstream_failure_to_bad_gateway() {
    let upstream = Router::new().route(
        "/example",
        get(|| async { StatusCode::SERVICE_UNAVAILABLE }),
    );
    let (status, body) = response_from_upstream(upstream).await;
    assert_eq!(status, StatusCode::BAD_GATEWAY);
    assert_eq!(body, r#"{"error":"example service unavailable"}"#);
}
