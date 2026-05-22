파일 업로드 서비스

📁 디렉토리 구조
file-storage/
│
├── main.py
├── database.py
├── config.py                  # 환경변수 관리
├── dependencies.py            # 공통 의존성 (get_db, get_current_user)
│
├── auth/
│   ├── __init__.py
│   ├── models.py              # User 테이블
│   ├── schemas.py             # RegisterRequest, LoginRequest, TokenResponse
│   ├── router.py              # POST /auth/register, /auth/login
│   ├── service.py             # 비밀번호 해싱, JWT 발급 로직
│   └── crud.py                # DB CRUD (get_user_by_email, create_user)
│
├── files/
│   ├── __init__.py
│   ├── models.py              # File 테이블
│   ├── schemas.py             # FileUploadResponse, FileListResponse
│   ├── router.py              # POST /files/upload, GET /files/, DELETE ...
│   ├── service.py             # 파일 저장/삭제 로직 (로컬 디스크)
│   └── crud.py                # DB CRUD (create_file, get_files_by_owner)
│
├── share/
│   ├── __init__.py
│   ├── models.py              # ShareLink 테이블
│   ├── schemas.py             # ShareLinkCreate, ShareLinkResponse
│   ├── router.py              # POST /share/{file_id}, GET /share/{token}
│   ├── service.py             # 토큰 생성, 만료 검증 로직
│   └── crud.py                # DB CRUD (create_link, get_link_by_token)
│
└── uploads/                   # 실제 파일 저장 폴더