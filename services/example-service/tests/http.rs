use axum::{body::to_bytes, http::Request};
use example_service::app;
use tower::ServiceExt;

#[tokio::test]
async fn example_endpoint_matches_its_http_contract() {
    let response = app()
        .oneshot(
            Request::builder()
                .uri("/example")
                .body(axum::body::Body::empty())
                .unwrap(),
        )
        .await
        .unwrap();
    assert_eq!(response.status(), axum::http::StatusCode::OK);
    let bytes = to_bytes(response.into_body(), 1024).await.unwrap();
    assert_eq!(
        bytes.as_ref(),
        br#"{"message":"Your Rust and Vue PoC is running."}"#
    );
}
