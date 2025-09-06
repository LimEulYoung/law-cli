# LawCLI 📚⚖️

> AI 기반 법령 및 판례 검색 CLI 도구

[![npm version](https://badge.fury.io/js/lawcli.svg)](https://badge.fury.io/js/lawcli)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

LawCLI는 명령줄에서 대화형으로 법령과 판례를 검색할 수 있는 AI 기반 도구입니다. 복잡한 법률 문서를 쉽고 빠르게 찾을 수 있도록 도와줍니다.

## ✨ 주요 특징

- 🖥️ **명령줄 인터페이스**: CMD/터미널에서 바로 사용 가능
- 🤖 **AI 기반 검색**: 자연어로 법률 문서 검색 (개발 예정)
- 📖 **법령 및 판례**: 한국 법령과 판례 데이터베이스 검색 (개발 예정)
- 🔍 **스마트 검색**: 키워드 검색과 벡터 검색을 결합한 정확한 검색 (개발 예정)
- 🌍 **크로스 플랫폼**: Windows, macOS, Linux 지원
- 📦 **간편 설치**: NPX로 한 번에 설치 및 실행

## 🚀 빠른 시작

### NPX로 즉시 실행 (권장)

```bash
npx lawcli@latest
```

### 설치 없이 바로 사용

```bash
# 최신 버전 실행
npx lawcli@latest

# 버전 확인
npx lawcli@latest --version

# 도움말 보기
npx lawcli@latest --help
```

## 📋 사용법

### 기본 사용법

1. **대화형 모드 시작**
   ```bash
   npx lawcli@latest
   ```

2. **명령어 입력**
   - `안녕하세요` 또는 `hello`: 환영 메시지
   - `도움말` 또는 `help`: 사용 가능한 명령어 보기
   - `quit`, `exit`, `q`: 프로그램 종료

### 현재 지원하는 기능

현재 버전(v0.1.0)에서는 기본적인 CLI 인터페이스와 사용자 상호작용만 지원합니다:

```
=========================================
            LawCLI v0.1.0              
      법령 및 판례 검색 시스템           
        AI-Powered Legal Search        
=========================================

대화형 모드를 시작합니다.
종료하려면 'quit' 또는 'exit'를 입력하세요.

LawCLI> 안녕하세요
안녕하세요! LawCLI에 오신 것을 환영합니다.

LawCLI> 도움말
사용 가능한 명령어:
  help, 도움말    - 이 도움말을 표시
  quit, exit, q   - 프로그램 종료

현재 버전에서는 기본적인 입력/출력만 지원합니다.
향후 업데이트에서 AI 기반 법률 검색 기능이 추가될 예정입니다.
```

## 🛠️ 개발자를 위한 정보

### 로컬 개발 환경 설정

1. **저장소 클론**
   ```bash
   git clone https://github.com/LimEulYoung/law-cli.git
   cd law-cli
   ```

2. **Python 가상환경 설정**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **로컬 실행**
   ```bash
   python lawcli/cli.py
   ```

### 프로젝트 구조

```
law-cli/
├── lawcli/
│   ├── __init__.py
│   └── cli.py              # 메인 CLI 애플리케이션
├── bin/
│   └── lawcli              # 실행 스크립트
├── package.json            # NPM 패키지 설정
├── install.js              # NPX 설치 스크립트
├── setup.py                # Python 패키지 설정
└── README.md               # 프로젝트 문서
```

## 🗺️ 로드맵

### v0.2.0 (계획)
- [ ] Elasticsearch 서버 연동
- [ ] MCP(Model Context Protocol) 서버 구현
- [ ] 기본 법령 데이터 수집

### v0.3.0 (계획)
- [ ] AI 기반 자연어 검색
- [ ] 판례 데이터베이스 추가
- [ ] 검색 결과 하이라이팅

### v1.0.0 (계획)
- [ ] 벡터 검색 + 키워드 검색 앙상블
- [ ] 고급 필터링 및 정렬
- [ ] 검색 결과 내보내기 기능

## 🤝 기여하기

프로젝트에 기여해주세요! 버그 리포트, 기능 제안, 풀 리퀘스트 모두 환영합니다.

1. 저장소를 포크합니다
2. 기능 브랜치를 만듭니다 (`git checkout -b feature/amazing-feature`)
3. 변경사항을 커밋합니다 (`git commit -m 'Add amazing feature'`)
4. 브랜치에 푸시합니다 (`git push origin feature/amazing-feature`)
5. 풀 리퀘스트를 열어주세요

## 📄 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 📞 연락처

- GitHub Issues: [이슈 등록](https://github.com/LimEulYoung/law-cli/issues)
- NPM Package: [lawcli](https://www.npmjs.com/package/lawcli)

## ⚠️ 면책 조항

이 도구는 법률 정보 검색을 돕는 보조 도구입니다. 법률 자문이나 전문적인 법률 서비스를 대체하지 않습니다. 중요한 법률 문제에 대해서는 반드시 전문 변호사와 상담하시기 바랍니다.
