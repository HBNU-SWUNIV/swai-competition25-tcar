# OSSW-Competition-WebShield  
소중한 오픈 소스 활용 SW 경진대회  

# 국립한밭대학교 TCAR팀  

—

## 주제  
- GPT API를 활용한 피싱 및 유해 사이트 실시간 탐지 크롬 확장 프로그램

—

## 팀 구성  
- 20222517 한하영 (영어영문학과)  
- 20222021 김주령 (컴퓨터공학과)  
- 20201738 서민재 (컴퓨터공학과)

—

## Project Background

### 개요  
인터넷 사용자들은 매일 다양한 웹사이트에 접속하지만, 피싱 사이트나 유해 콘텐츠에 대한 사전 경고 없이 피해를 입는 사례가 증가하고 있습니다.  
WebShield는 크롬 브라우저 환경에서 사용자가 방문하는 웹사이트의 내용을 실시간으로 분석하여, GPT를 활용해 **피싱 가능성**, **유해성**, **정상 여부**를 판단해주는 보안 확장 프로그램입니다.

### 필요성  
- 사용자는 URL만 보고 위험 여부를 판단하기 어려움  
- 기존 블랙리스트 기반 솔루션은 제로데이(신규 피싱)에 대응 불가  
- AI 기반 정적 분석이 보안 분야에서도 필수적으로 활용될 필요성 대두

—

## 프로젝트 내용

### 구현 내용  
- 사용자 방문 페이지에서 텍스트 콘텐츠 자동 수집 (HTML 파싱)
- 불용어 제거 및 핵심 키워드 추출
- FastAPI 서버를 통해 GPT API 요청
- GPT의 응답을 바탕으로 "정상", "피싱 가능성", "유해 가능성" 판단
- 크롬 확장 아이콘 색상 변경 및 결과 팝업 출력

### 기대 효과  
- 신규 피싱/유해 사이트 탐지 가능 (GPT 기반)
- 사용자 UX를 해치지 않는 자연스러운 보안 도우미
- 텍스트 중심 판단으로 과잉 탐지 최소화
- 경량 크롬 확장으로 누구나 쉽게 설치 가능

—

## 개발환경

### DBMS  
- 별도 DB 사용 없음 (실시간 분석 기반)

### 개발 언어 및 프레임워크  
- **Frontend:** JavaScript (Chrome Extension API)  
- **Backend:** Python 3.10+, FastAPI, Uvicorn  
- **AI Model:** OpenAI GPT-3.5 API  
- **환경 변수 관리:** python-dotenv  

### 기타 도구  
- Git / GitHub  
- 크롬 확장 프로그램 Manifest V3  
- 환경 테스트용 curl, Postman  
- ChatGPT 프롬프트 최적화 및 분석 기준 설계

—

## 프로젝트 구조
WebShield
├── webshield-extension/
│   ├── content.js
│   ├── background.js
│   ├── popup.html / popup.js
│   └── manifest.json
├── webshield-backend/
│   ├── main.py
│   ├── prompt_generator.py
│   ├── openai_client.py
│   └── requirements.txt
└── .env
