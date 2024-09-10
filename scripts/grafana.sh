#!/bin/bash

docker run --rm --network services -p 10.2.0.134:3000:3000 grafana/grafana
