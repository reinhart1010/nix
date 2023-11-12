---
layout: page
title: common/cake (한국어)
description: "CakePHP 프레임 워크용 명령어 라인 프로세서."
content_hash: 01dc70c0fd57d9799ac283f4168a53a304f7e0d8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cake.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cake.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cake

CakePHP 프레임 워크용 명령어 라인 프로세서.
더 많은 정보: <https://cakephp.org>.

- 현재 앱 및 사용 가능한 명령어에 대한 기본 정보 표시:

`cake`

- 사용 가능한 경로 리스트 표시:

`cake routes`

- 구성 캐시 지우기:

`cake cache clear_all`

- 메타데이터 캐시 구축:

`cake schema_cache build --connection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연결할것</span>

- 메타데이터 캐시 지우기:

`cake schema_cache clear`

- 단일 캐시 테이블 지우기:

`cake schema_cache clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>

- 개발 웹 서버 시작 (포트 기본값 8765):

`cake server`

- REPL 대화형 쉘 인스턴스 시작:

`cake console`
