#!/usr/bin/env bash

uvicorn api.main:app --host 127.0.0.1 --port 8000 &

streamlit run app/main.py \
--server.port ${PORT:-7860} \
--server.address 0.0.0.0