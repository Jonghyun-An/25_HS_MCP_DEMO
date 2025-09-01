# Korean Weather MCP Server
from fastmcp import FastMCP
from typing import Dict, Optional
import uvicorn
import argparse
import sys

# 한국 주요 도시들의 날씨 데이터 (예시)
KOREAN_CITIES_WEATHER = {
    "서울": {
        "temperature": "15°C",
        "humidity": "65%",
        "condition": "맑음",
        "wind_speed": "5km/h"
    },
    "부산": {
        "temperature": "18°C", 
        "humidity": "70%",
        "condition": "구름많음",
        "wind_speed": "8km/h"
    },
    "대구": {
        "temperature": "16°C",
        "humidity": "60%", 
        "condition": "맑음",
        "wind_speed": "3km/h"
    },
    "인천": {
        "temperature": "14°C",
        "humidity": "68%",
        "condition": "흐림",
        "wind_speed": "6km/h"
    },
    "광주": {
        "temperature": "17°C",
        "humidity": "62%",
        "condition": "맑음", 
        "wind_speed": "4km/h"
    },
    "대전": {
        "temperature": "15°C",
        "humidity": "64%",
        "condition": "구름많음",
        "wind_speed": "5km/h"
    },
    "울산": {
        "temperature": "19°C",
        "humidity": "72%",
        "condition": "맑음",
        "wind_speed": "7km/h"
    },
    "수원": {
        "temperature": "14°C",
        "humidity": "66%", 
        "condition": "흐림",
        "wind_speed": "4km/h"
    },
    "고양": {
        "temperature": "13°C",
        "humidity": "63%",
        "condition": "맑음",
        "wind_speed": "5km/h"
    },
    "용인": {
        "temperature": "14°C",
        "humidity": "65%",
        "condition": "구름많음", 
        "wind_speed": "3km/h"
    }
}

# FastMCP 인스턴스 생성
mcp = FastMCP("Korean Weather Service")

@mcp.tool()
def get_weather(city_name: str) -> Dict:
    """
    한국 도시의 날씨 정보를 반환합니다.
    
    Args:
        city_name: 날씨를 조회할 한국 도시 이름
        
    Returns:
        해당 도시의 날씨 정보 딕셔너리
    """
    if city_name in KOREAN_CITIES_WEATHER:
        return {
            "city": city_name,
            "weather": KOREAN_CITIES_WEATHER[city_name],
            "status": "success"
        }
    else:
        available_cities = list(KOREAN_CITIES_WEATHER.keys())
        return {
            "city": city_name,
            "weather": None,
            "status": "error",
            "message": f"'{city_name}' 도시의 날씨 정보가 없습니다.",
            "available_cities": available_cities
        }

@mcp.tool()
def get_all_cities() -> Dict:
    """
    지원하는 모든 한국 도시 목록을 반환합니다.
    
    Returns:
        지원 도시 목록과 각 도시의 날씨 정보
    """
    return {
        "total_cities": len(KOREAN_CITIES_WEATHER),
        "cities": list(KOREAN_CITIES_WEATHER.keys()),
        "all_weather_data": KOREAN_CITIES_WEATHER
    }

def main():
    """메인 함수 - 명령행 인수를 파싱하여 적절한 전송 모드로 서버 실행"""
    parser = argparse.ArgumentParser(description="Korean Weather MCP Server")
    parser.add_argument(
        "--transport", 
        choices=["stdio", "sse", "streamable-http"],
        default="stdio",
        help="전송 방식 선택 (기본값: stdio)"
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0", 
        help="SSE/Streamable-HTTP 모드용 호스트 주소 (기본값: 0.0.0.0)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8111,
        help="SSE/Streamable-HTTP 모드용 포트 번호 (기본값: 8111)"
    )
    
    args = parser.parse_args()
    
    print(f"한국 날씨 서버를 {args.transport} 모드로 시작합니다...", file=sys.stderr)
    
    if args.transport == "stdio":
        # STDIO 모드 - 표준입출력을 통한 통신
        mcp.run(transport="stdio")
    elif args.transport == "sse":
        # SSE (Server-Sent Events) 모드 - HTTP 기반
        print(f"SSE 서버가 http://{args.host}:{args.port}에서 실행됩니다", file=sys.stderr)
        mcp.run(transport="sse", host=args.host, port=args.port)
    elif args.transport == "streamable-http":
        # Streamable-HTTP 모드 - HTTP 기반 스트리밍
        print(f"Streamable-HTTP 서버가 http://{args.host}:{args.port}에서 실행됩니다", file=sys.stderr)
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    else:
        print(f"지원하지 않는 전송 모드: {args.transport}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
