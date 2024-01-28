#!/usr/bin/with-contenv bashio
COPY server.py /web/server.py
COPY index.html /index.html
echo "EnergAI Started"
python3 server.py
echo "EnergAI Webserver Started"
