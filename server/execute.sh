#!/bin/bash
# 현재 경로 저장
BASE_DIR="$(pwd)"

# 실행할 스크립트 경로
SCRIPT_PATH="$BASE_DIR/server/main.py"

# 실행 권한 부여 (필요할 경우)
chmod +x "$SCRIPT_PATH"

# 실행
python "$SCRIPT_PATH"
# python -m uvicorn main:app --reload --port 8000