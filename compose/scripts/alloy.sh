#!/bin/bash

alloy run \
        ./config.alloy \
        --storage.path=./data \
        --server.http.listen-addr=10.2.0.134:12345 \
        --stability.level=experimental
