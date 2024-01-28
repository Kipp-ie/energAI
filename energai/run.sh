#!/usr/bin/with-contenv bashio
echo "EnergAI Started"
cd "$(dirname "$0")" || exit

# Run the Python script
python server.py
echo "EnergAI Webserver Started"
