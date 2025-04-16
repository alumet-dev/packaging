ARG BASE_IMAGE=ubuntu:24.04
FROM $BASE_IMAGE AS runtime

ARG ALUMET_VERSION=0.8
LABEL org.opencontainers.image.authors="maintainers@alumet.dev" \
	org.opencontainers.image.documentation="https://alumet-dev.github.io/user-book" \
	org.opencontainers.image.source="https://github.com/alumet-dev/alumet" \
	org.opencontainers.image.version="$ALUMET_VERSION" \
	org.opencontainers.image.vendor="alumet-dev" \
	org.opencontainers.image.licenses="EUPL-1.2" \
	org.opencontainers.image.title="alumet-agent based on Ubuntu OS" \
	org.opencontainers.image.description="Alumet is a modular tool that measures energy consumption and performance metrics. "

ARG ARTIFACT_FILE=alumet-agent_0.8-1_amd64_ubuntu_24.04.deb
COPY $ARTIFACT_FILE /tmp/

RUN apt update -y && \ 
    apt install -y /tmp/$ARTIFACT_FILE && \
    rm -f /tmp/$ARTIFACT_FILE && \
    rm /usr/bin/alumet-agent && mv /usr/lib/alumet-agent /usr/bin/alumet-agent && \
    groupadd -r alumet && \
    useradd -r -g alumet alumet && \
    mkdir /app && \
    chown alumet:alumet /usr/bin/alumet-agent /etc/alumet/alumet-config.toml /app; \
    setcap "cap_sys_nice+ep cap_perfmon=ep" "/usr/bin/alumet-agent"

USER alumet
WORKDIR /app

ENTRYPOINT ["/usr/bin/alumet-agent"]
CMD ["--config", "/etc/alumet/alumet-config.toml", "--plugins", "csv,perf,procfs,socket-control", "--output-file", "/app/alumet-output.csv"]
