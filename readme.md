# Django SandBox Template

- `Last Update`: 2025.06.20

## TOC

- [README](#README)
- [Requirement](#Requirement)
- [Structure](#Structure)

### README

- 초기에 django project 생성 후 설정해야되는 부분을 template으로 만들고 가져다 쓰기 위해 생성함

### Requirement

- `Python` 3.11.5

### Structure

- `apps`
    - `apps` 디렉토리는 django의 app을 다루기 위해서 만듬
    - `app` 다루기
        - django의 app은 작은 단위로 쪼개서 만드는 것이 좋음
        - 본 프로젝트의 컨셉은 `apps 디렉토리` 안에서 모든 app 을 관리하도록 구성함
        - 사용하려는 프로젝트의 컨셉에 맞게 app 구조를 변경해도 상관없음
- `config`
    - `django project` 환경설정 파일
        - `setting`의 디렉토리에 `local`만 만들어 둠
            - `local` 에 포함된 내용
                - DATABASE
                - INSTALLED_APPS
                - ALLOWED_HOSTS
                - Internatinonalization 설정
                - LOGGING
    - `DATABASE`
        - `local.py`에 설정된 DATABASE 환경은 mysql을 기준으로 함
            - USERNAME: root
            - PASSWORD: 1234
            - DB_PORT: 9901



