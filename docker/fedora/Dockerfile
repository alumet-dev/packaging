ARG BASE_IMAGE=fedora:42
FROM $BASE_IMAGE AS runtime

ARG ALUMET_VERSION=0.8
LABEL org.opencontainers.image.authors="maintainers@alumet.dev" \
	org.opencontainers.image.documentation="https://alumet-dev.github.io/user-book" \
	org.opencontainers.image.source="https://github.com/alumet-dev/alumet" \
	org.opencontainers.image.version="$ALUMET_VERSION" \
	org.opencontainers.image.vendor="alumet-dev" \
	org.opencontainers.image.licenses="EUPL-1.2" \
	org.opencontainers.image.title="alumet-agent based on Fedora OS" \
	org.opencontainers.image.description="Alumet is a modular tool that measures energy consumption and performance metrics. "

ARG ARTIFACT_FILE=alumet-agent-0.8.0-1.fc42.x86_64.rpm
COPY $ARTIFACT_FILE /tmp/

RUN dnf install -y /tmp/$ARTIFACT_FILE && \
    rm -f /tmp/$ARTIFACT_FILE && \
    rm /usr/bin/alumet-agent && \
    mv /usr/lib/alumet-agent /usr/bin/alumet-agent && \
    dnf install -y util-linux && \
    dnf clean all && \
    groupadd -r alumet && \
    useradd -r -g alumet alumet && \
    mkdir /app && \
    chown alumet:alumet /usr/bin/alumet-agent /etc/alumet/alumet-config.toml /app; \
    setcap "cap_sys_nice+ep cap_perfmon=ep" "/usr/bin/alumet-agent"

USER alumet
WORKDIR /app

ENTRYPOINT ["/usr/bin/alumet-agent"]
CMD ["--config", "/etc/alumet/alumet-config.toml", "--plugins", "csv,perf,procfs,socket-control", "--output-file", "/app/alumet-output.csv"]
