project 
│
├── bot/                           # discord.py 기반 챗봇
│   ├── __init__.py
│   ├── bot.py                    # Discord Bot 실행 (gateway 이벤트 전용)
│   ├── cogs/
│   │   ├── greetings.py           # 입장 환영 / 상태 감지 등
│   │   └── motivational.py        # 동기부여 멘트
│
├── server/
│   ├── discord_interactions/          # FastAPI 서버 (웹훅 처리 전용)
│   ├── __init__.py
│   ├── main.py                        # FastAPI 실행 진입점 (uvicorn) 
│   ├── routes.py                  # FastAPI 라우트
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── slash_command_handlers.py
│   │   ├── component_handlers.py
│   │   └── modal_handlers.py
│   │   └── register_commands.py
│   └── services/
│       ├── __init__.py
│       └── goal_api.py        # REST API 호출 로직
│
├── requirements.txt
└── README.md
