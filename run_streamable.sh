#!/bin/bash
# FastMCP Streamable-HTTP 모드 실행

HOST=${1:-"127.0.0.1"}
PORT=${2:-8111}

echo "🚀 FastMCP Streamable-HTTP 서버를 http://$HOST:$PORT에서 시작합니다..."
echo "종료하려면 Ctrl+C를 누르세요."

# 표준 FastMCP 구현 사용 (FastMCP CLI 대신)
uv run python weather.py --transport streamable-http --host "$HOST" --port "$PORT"
