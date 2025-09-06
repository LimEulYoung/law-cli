#!/usr/bin/env python3
"""
LawCLI - 법령 및 판례 검색 시스템
AI 기반 법률 문서 검색 CLI 도구
"""

import sys
import argparse
from typing import Optional

def print_banner():
    """CLI 시작 배너 출력"""
    banner = """
=========================================
            LawCLI v0.1.0              
      법령 및 판례 검색 시스템           
        AI-Powered Legal Search        
=========================================
    """
    print(banner)

def interactive_mode():
    """대화형 모드 실행"""
    print("대화형 모드를 시작합니다.")
    print("종료하려면 'quit' 또는 'exit'를 입력하세요.\n")
    
    while True:
        try:
            user_input = input("LawCLI> ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("LawCLI를 종료합니다. 안녕히 가세요!")
                break
            
            if not user_input:
                continue
                
            # 현재는 간단한 응답만 제공
            if "안녕" in user_input or "hello" in user_input.lower():
                print("안녕하세요! LawCLI에 오신 것을 환영합니다.")
            elif "도움말" in user_input or "help" in user_input.lower():
                print_help()
            else:
                print(f"입력하신 내용: '{user_input}'")
                print("Hello World! 현재는 기본 응답만 제공합니다.")
                print("곧 AI 기반 법률 검색 기능이 추가될 예정입니다.\n")
                
        except KeyboardInterrupt:
            print("\n\nKeyboard interrupt 감지. LawCLI를 종료합니다.")
            break
        except EOFError:
            print("\nEOF 감지. LawCLI를 종료합니다.")
            break

def print_help():
    """도움말 출력"""
    help_text = """
사용 가능한 명령어:
  help, 도움말    - 이 도움말을 표시
  quit, exit, q   - 프로그램 종료
  
현재 버전에서는 기본적인 입력/출력만 지원합니다.
향후 업데이트에서 AI 기반 법률 검색 기능이 추가될 예정입니다.
"""
    print(help_text)

def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(
        description="LawCLI - AI 기반 법령 및 판례 검색 시스템",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--version", "-v",
        action="version",
        version="LawCLI 0.1.0"
    )
    
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="대화형 모드로 실행"
    )
    
    args = parser.parse_args()
    
    print_banner()
    
    # 기본적으로 대화형 모드 실행
    if len(sys.argv) == 1 or args.interactive:
        interactive_mode()
    
if __name__ == "__main__":
    main()