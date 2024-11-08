---
layout: page
title: common/poetry (한국어)
description: "Python 패키지 및 의존성을 관리."
content_hash: ab06fc27ac9234bc0b5cc09dff993b142cf5c420
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/common/poetry.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/poetry.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/poetry.html
    icon: bi bi-globe
tldri18n_status: 2
---
# poetry

Python 패키지 및 의존성을 관리.
같이 보기: `asdf`.
더 많은 정보: <https://python-poetry.org/docs/cli/>.

- 특정 이름으로 디렉토리에 새 Poetry 프로젝트 생성:

`poetry new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- 현재 디렉토리의 `pyproject.toml` 파일에 의존성과 그 하위 의존성 설치 및 추가:

`poetry add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성</span>

- 현재 디렉토리의 `pyproject.toml` 파일을 사용하여 프로젝트 의존성 설치:

`poetry install`

- 현재 디렉토리를 새 Poetry 프로젝트로 상호작용 방식으로 초기화:

`poetry init`

- 모든 의존성의 최신 버전 가져오고 `poetry.lock` 업데이트:

`poetry update`

- 프로젝트의 가상 환경 내에서 명령어 실행:

`poetry run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- `pyproject.toml`에서 프로젝트의 버전 증가:

`poetry version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patch|minor|major|prepatch|preminor|premajor|prerelease</span>

- 프로젝트의 가상 환경 내에서 셸 시작:

`poetry shell`
