use axum::{Json, Router, routing::get};
use serde::Serialize;

#[derive(Serialize)]
struct ExampleResponse {
    message: &'static str,
}

pub fn app() -> Router {
    Router::new()
        .route("/health", get(|| async { "ok" }))
        .route(
            "/example",
            get(|| async {
                Json(ExampleResponse {
                    message: "Your Rust and Vue PoC is running.",
                })
            }),
        )
}
