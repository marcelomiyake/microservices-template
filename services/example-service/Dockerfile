FROM rust:1.98-bookworm AS builder
WORKDIR /workspace
COPY Cargo.toml Cargo.lock ./
COPY services ./services
RUN cargo build --locked --release --package example-service

FROM gcr.io/distroless/cc-debian12:nonroot
COPY --from=builder /workspace/target/release/example-service /usr/local/bin/example-service
EXPOSE 8082
USER 65532:65532
ENTRYPOINT ["/usr/local/bin/example-service"]
