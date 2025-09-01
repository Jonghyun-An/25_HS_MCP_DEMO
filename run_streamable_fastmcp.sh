#!/bin/bash
# FastMCP CLI를 사용한 Streamable-HTTP 모드 실행

HOST=${1:-"127.0.0.1"}
PORT=${2:-8111}

echo "🚀 FastMCP CLI로 Streamable-HTTP 서버를 http://$HOST:$PORT에서 시작합니다..."
echo "종료하려면 Ctrl+C를 누르세요."

# FastMCP CLI 사용
uv run fastmcp run weather.py:mcp --transport streamable-http --host "$HOST" --port "$PORT"
