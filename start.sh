#!/bin/bash

# Запуск FastAPI в фоне
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Запуск Nginx
nginx -g "daemon off;"