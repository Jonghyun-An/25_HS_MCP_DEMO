# 한국 날씨 MCP 서버

한국 주요 도시들의 날씨 정보를 제공하는 MCP (Model Context Protocol) 서버입니다.

## 지원 도시
- 서울, 부산, 대구, 인천, 광주, 대전, 울산, 수원, 고양, 용인

## 예시 프롬프트

```
날씨를 조회하고 싶어 현재 도시들의 리스트를 받아서 랜덤으로 하나 선택해서 해당 도시의 날씨 확인해줘
```

## mcp.json

```json
"korean-weather-sse": {
      "url": "http://localhost:8111/sse"
    },
    "korean-weather-stdio": {
      "command": "/home/rudder/25_MCP_DEMO/run_stdio.sh",
      "args": [],
      "description": "한국 날씨 정보를 제공하는 MCP 서버 (UV 스크립트 + STDIO)",
      "env": {
        "PYTHONUNBUFFERED": "1"
      }
    },
    "korean-weather-streamable-http": {
      "url": "http://localhost:8111/mcp",
      "description": "한국 날씨 정보를 제공하는 MCP 서버 (Streamable-HTTP 모드)",
      "transport": "streamable-http"
    }
```

## 지원 전송 모드

### 1. STDIO 모드 (기본값)
표준입출력을 통한 통신 방식으로, MCP 클라이언트가 프로세스를 직접 시작합니다.

#### 실행 방법:
```bash
# 직접 실행
uv run python weather.py --transport stdio

# 스크립트로 실행
./run_stdio.sh
# 또는 통합 스크립트 사용
./run.sh stdio
```

#### MCP 설정:
Claude Desktop에서 사용하려면 `claude_desktop_config.json` 파일을 Claude Desktop 설정 폴더에 복사하세요.

### 2. SSE (Server-Sent Events) 모드
HTTP 기반 통신 방식으로, 웹 브라우저나 HTTP 클라이언트에서 접근 가능합니다.

#### 실행 방법:
```bash
# 직접 실행 (기본 포트: 8111)
uv run python weather.py --transport sse --host 0.0.0.0 --port 8111

# 스크립트로 실행
./run_sse.sh localhost 8111
# 또는 통합 스크립트 사용
./run.sh sse localhost 8111
```

#### 접속 URL:
- 서버: `http://localhost:8111/sse`

### 3. Streamable-HTTP 모드
HTTP 기반 스트리밍 통신 방식으로, MCP 클라이언트와의 실시간 통신을 지원합니다.

#### 실행 방법:
```bash
# 직접 실행 (기본 포트: 8111)
uv run python weather.py --transport streamable-http --host 0.0.0.0 --port 8111

# 통합 스크립트 사용
./run.sh streamable-http localhost 8111

# FastMCP CLI 사용 (권장)
./run.sh fastmcp localhost 8111
```

#### 접속 URL:
- Streamable-HTTP: `http://localhost:8111/mcp`

## 사용 가능한 도구 (Tools)

### 1. `get_weather(city_name: str)`
특정 도시의 날씨 정보를 반환합니다.

**매개변수:**
- `city_name`: 날씨를 조회할 한국 도시 이름

**반환값:**
```json
{
  "city": "서울",
  "weather": {
    "temperature": "15°C",
    "humidity": "65%",
    "condition": "맑음",
    "wind_speed": "5km/h"
  },
  "status": "success"
}
```

### 2. `get_all_cities()`
지원하는 모든 한국 도시 목록과 각 도시의 날씨 정보를 반환합니다.

**반환값:**
```json
{
  "total_cities": 10,
  "cities": ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "수원", "고양", "용인"],
  "all_weather_data": {
    "서울": {
      "temperature": "15°C",
      "humidity": "65%",
      "condition": "맑음",
      "wind_speed": "5km/h"
    }
  }
}
```

## 설정 파일

각 전송 모드별로 MCP 클라이언트 설정 파일을 제공합니다:

- `mcp_config_stdio.json`: STDIO 모드용 설정 (UV 직접 실행)
- `mcp_config_stdio_bash.json`: STDIO 모드용 설정 (Bash 스크립트 실행)
- `mcp_config_sse.json`: SSE 모드용 설정
- `mcp_config_streamable.json`: Streamable 모드용 설정
- `claude_desktop_config.json`: Claude Desktop 전용 설정

## 요구사항

이 프로젝트는 UV 패키지 매니저를 사용합니다:

```bash
# UV 설치 (아직 설치하지 않았다면)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 의존성 자동 설치 (uv run 명령어 사용 시)
# 또는 수동으로 의존성 설치
uv sync
```

**필요한 패키지:**
- `fastmcp>=2.11.3` - MCP 서버 프레임워크
- `uvicorn>=0.35.0` - ASGI 웹 서버

## 예제 사용법

```bash
# 통합 스크립트 사용 (권장)
./run.sh stdio                         # STDIO 모드
./run.sh sse localhost 8111           # SSE 모드  
./run.sh streamable-http 0.0.0.0 8111 # Streamable-HTTP 모드
./run.sh fastmcp 127.0.0.1 8111      # FastMCP CLI 모드

# 직접 실행
uv run python weather.py --transport stdio
uv run python weather.py --transport sse --port 8111  
uv run python weather.py --transport streamable-http --port 8111
```

## 디버깅 및 로그

모든 서버 시작 메시지는 `stderr`로 출력되므로, MCP 프로토콜 통신과 구분됩니다.

```bash
# 로그 확인 (STDIO 모드 제외)
uv run python weather.py --transport sse 2> server.log
```
