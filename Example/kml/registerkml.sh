#!/bin/sh
curl -X POST -H "Content-Type: application/json" -d @./model.json \
http://ql2:9187/kml/model/instance/create