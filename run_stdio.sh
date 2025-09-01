#!/bin/bash
# UV를 사용하여 STDIO 모드로 한국 날씨 서버 실행

# 스크립트가 있는 디렉토리로 이동
cd "$(dirname "$0")"

echo "UV를 사용하여 STDIO 모드로 한국 날씨 서버를 시작합니다..."

# UV 환경에서 Python 스크립트 실행
exec uv run --project . python weather.py --transport stdio