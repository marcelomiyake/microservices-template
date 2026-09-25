use axum::{Json, Router, extract::State, http::StatusCode, routing::get};
use serde::{Deserialize, Serialize};

#[derive(Clone)]
pub struct AppState {
    pub client: reqwest::Client,
    pub example_service_url: String,
}

#[derive(Deserialize, Serialize)]
struct ExampleResponse {
    message: String,
}

#[derive(Serialize)]
struct ErrorResponse {
    error: &'static str,
}

async fn example(
    State(state): State<AppState>,
) -> Result<Json<ExampleResponse>, (StatusCode, Json<ErrorResponse>)> {
    let url = format!(
        "{}/example",
        state.example_service_url.trim_end_matches('/')
    );
    let response = state
        .client
        .get(url)
        .send()
        .await
        .map_err(|_| unavailable())?;
    if !response.status().is_success() {
        return Err(unavailable());
    }
    response
        .json::<ExampleResponse>()
        .await
        .map(Json)
        .map_err(|_| unavailable())
}

fn unavailable() -> (StatusCode, Json<ErrorResponse>) {
    (
        StatusCode::BAD_GATEWAY,
        Json(ErrorResponse {
            error: "example service unavailable",
        }),
    )
}

pub fn app(state: AppState) -> Router {
    Router::new()
        .route("/health", get(|| async { "ok" }))
        .route("/api/example", get(example))
        .with_state(state)
}
