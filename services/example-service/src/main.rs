use example_service::app;
use std::{
    env,
    net::{IpAddr, SocketAddr},
};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let port = env::var("PORT").unwrap_or_else(|_| "8082".into()).parse()?;
    let bind_address: IpAddr = env::var("BIND_ADDRESS")
        .unwrap_or_else(|_| "127.0.0.1".into())
        .parse()?;
    let addr = SocketAddr::new(bind_address, port);
    let listener = tokio::net::TcpListener::bind(addr).await?;
    println!("example-service listening on http://{addr}");
    axum::serve(listener, app()).await?;
    Ok(())
}
