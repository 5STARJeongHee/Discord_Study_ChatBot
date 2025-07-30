# Discord_Study_ChatBot

## project structure

chat/
│
├── bot.py                # 봇 실행 진입점
│
├── commands/             # 슬래시 커맨드, 텍스트 커맨드 등 - controller 같은 느낌
│   └── default_commands.py
│
├── events/               # on_member_join, on_message 등 이벤트 핸들러
│   └── user_tracking.py
│
├── views/                # 여러 UI View(버튼, 모달 등)
│   ├── help_view.py
│   ├── goal_button_views.py
│   └── ... (각종 View)
│
├── modals/               # Modal(Form) 관련 클래스
│   ├── goal_form.py
│   ├── goal_edit_form.py
│   └── ...
│
├── handlers/             # 반복되는 로직, 서비스 모듈
|   ├── goal_handler.py
│   └── ...
|
├── api/                  # 외부 API 연동, API 호출 함수 등
│   └── goal_api.py
│
├── config/               # 설정 파일
│   ├── config.py
│   └── properties.py
│
├── utils/                # 유틸리티 함수, 공통 모듈
│   └── helpers.py
│
└── requirements.txt


## 봇 실행 진입점
bot.py

## 봇 interaction 구조

               [bot.py 봇]
               (봇 메시지 전송 / 일반 커맨드 처리)
                         │
                ------------------
               │                  │
     [사용자 상호작용]         [버튼 클릭]
   (슬래시 명령 호출)        (components v2)
               │                  │
               ▼                  ▼
      [bot.py View 핸들러]     →  [FastAPI /interactions 엔드포인트]
               │                           └ custom_id 기반 응답
