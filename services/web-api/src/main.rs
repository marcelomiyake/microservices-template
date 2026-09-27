use std::{
    env,
    net::{IpAddr, SocketAddr},
    time::Duration,
};
use web_api::{AppState, app};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let port = env::var("PORT").unwrap_or_else(|_| "8081".into()).parse()?;
    let example_service_url =
        env::var("EXAMPLE_SERVICE_URL").unwrap_or_else(|_| "http://127.0.0.1:8082".into());
    let client = reqwest::Client::builder()
        .timeout(Duration::from_secs(3))
        .build()?;
    let state = AppState {
        client,
        example_service_url,
    };
    let bind_address: IpAddr = env::var("BIND_ADDRESS")
        .unwrap_or_else(|_| "127.0.0.1".into())
        .parse()?;
    let addr = SocketAddr::new(bind_address, port);
    let listener = tokio::net::TcpListener::bind(addr).await?;
    println!("web-api listening on http://{addr}");
    axum::serve(listener, app(state)).await?;
    Ok(())
}
