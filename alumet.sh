#!/bin/bash

DEFAULT_CONFIG_FILE=/etc/alumet/alumet-config.toml
ALUMET_AGENT=/usr/lib/alumet-agent
if [ -z ${ALUMET_CONFIG+x} ]; then
  export ALUMET_CONFIG="$DEFAULT_CONFIG_FILE"
fi
"$ALUMET_AGENT" "$@"
