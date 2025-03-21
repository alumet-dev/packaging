ARG BUILDER_IMAGE=registry.access.redhat.com/ubi9:9.5
ARG BASE_IMAGE=registry.access.redhat.com/ubi9-micro:9.5
FROM $BUILDER_IMAGE AS builder

ARG ALUMET_VERSION=0.8
LABEL org.opencontainers.image.authors="maintainers@alumet.dev" \
	org.opencontainers.image.documentation="https://alumet-dev.github.io/user-book" \
	org.opencontainers.image.source="https://github.com/alumet-dev/alumet" \
	org.opencontainers.image.version="$ALUMET_VERSION" \
	org.opencontainers.image.vendor="alumet-dev" \
	org.opencontainers.image.licenses="EUPL-1.2" \
	org.opencontainers.image.title="alumet-agent based on Redhat UBI OS" \
	org.opencontainers.image.description="Alumet is a modular tool that measures energy consumption and performance metrics. "

ARG ARTIFACT_FILE=alumet-agent-0.8.0-1.ubi.9.5.x86_64.rpm
COPY ${ARTIFACT_FILE} /tmp/

RUN dnf install -y /tmp/$ARTIFACT_FILE && rm -f /tmp/$ARTIFACT_FILE

FROM $BASE_IMAGE AS runtime

ARG LIBSSL_VERSION=3
ARG LIBCRYPTO_VERSION=3
ARG LIBZ_VERSION=1
COPY --from=builder /usr/lib/alumet-agent /usr/bin/alumet-agent
COPY --from=builder /etc/alumet/alumet-config.toml /etc/alumet/alumet-config.toml
COPY --from=builder /lib64/libssl.so.${LIBSSL_VERSION} /lib64/
COPY --from=builder /lib64/libcrypto.so.${LIBCRYPTO_VERSION} /lib64/
COPY --from=builder /lib64/libz.so.${LIBZ_VERSION} /lib64/

RUN echo "alumet:x:1000:" >> /etc/group && \
    echo "alumet:x:1000:1000::/home/alumet:/sbin/nologin" >> /etc/passwd && \
	mkdir -p /app /home/alumet && \
	chown alumet:alumet /usr/bin/alumet-agent /etc/alumet/alumet-config.toml /app # chown makes alumet-agent bin to be duplicated by docker which increase image size

USER alumet
WORKDIR /app

ENTRYPOINT ["/usr/bin/alumet-agent"]
CMD ["--config", "/etc/alumet/alumet-config.toml", "--plugins", "csv,perf,procfs,socket-control", "--output-file", "/app/alumet-output.csv"]
