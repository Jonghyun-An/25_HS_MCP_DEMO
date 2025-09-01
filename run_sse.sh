#!/bin/bash
# SSE 모드로 한국 날씨 서버 실행

HOST=${1:-"0.0.0.0"}
PORT=${2:-8111}

echo "SSE 서버를 http://$HOST:$PORT에서 시작합니다..."
echo "종료하려면 Ctrl+C를 누르세요."
uv run python weather.py --transport sse --host "$HOST" --port "$PORT"
