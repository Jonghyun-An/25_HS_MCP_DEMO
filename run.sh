#!/bin/bash
# 한국 날씨 MCP 서버 실행 스크립트

TRANSPORT=${1:-"stdio"}
HOST=${2:-"0.0.0.0"}
PORT=${3:-8111}

case $TRANSPORT in
    stdio)
        echo "STDIO 모드로 한국 날씨 서버를 시작합니다..."
        uv run python weather.py --transport stdio
        ;;
    sse)
        echo "SSE 서버를 http://$HOST:$PORT에서 시작합니다..."
        echo "종료하려면 Ctrl+C를 누르세요."
        uv run python weather.py --transport sse --host "$HOST" --port "$PORT"
        ;;
    streamable-http)
        echo "🚀 Streamable-HTTP 서버를 http://$HOST:$PORT에서 시작합니다..."
        echo "종료하려면 Ctrl+C를 누르세요."
        uv run python weather.py --transport streamable-http --host "$HOST" --port "$PORT"
        ;;
    fastmcp)
        echo "🚀 FastMCP CLI로 Streamable-HTTP 서버를 http://$HOST:$PORT에서 시작합니다..."
        echo "종료하려면 Ctrl+C를 누르세요."
        uv run fastmcp run weather.py:mcp --transport streamable-http --host "$HOST" --port "$PORT"
        ;;
    *)
        echo "사용법: $0 [stdio|sse|streamable-http|fastmcp] [host] [port]"
        echo "예시:"
        echo "  $0 stdio                    # STDIO 모드"
        echo "  $0 sse localhost 8111       # SSE 모드"
        echo "  $0 streamable-http 0.0.0.0 8111  # Streamable-HTTP 모드"
        echo "  $0 fastmcp 127.0.0.1 8111   # FastMCP CLI 모드"
        exit 1
        ;;
esac