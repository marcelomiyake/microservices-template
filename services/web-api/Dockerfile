FROM rust:1.98-bookworm AS builder
WORKDIR /workspace
COPY Cargo.toml Cargo.lock ./
COPY services ./services
RUN cargo build --locked --release --package web-api

FROM gcr.io/distroless/cc-debian12:nonroot
COPY --from=builder /workspace/target/release/web-api /usr/local/bin/web-api
EXPOSE 8081
USER 65532:65532
ENTRYPOINT ["/usr/local/bin/web-api"]
