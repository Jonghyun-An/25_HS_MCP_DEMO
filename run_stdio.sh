#!/bin/bash
# STDIO 모드로 한국 날씨 서버 실행

echo "STDIO 모드로 한국 날씨 서버를 시작합니다..."
uv run python weather.py --transport stdio
