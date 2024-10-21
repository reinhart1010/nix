---
layout: page
title: common/fossa (한국어)
description: "Fossa 서비스용 CLI - 종속성 라이센스에 대한 실시간 라이센스 감사, 취약성 검색 및 보고서를 생성."
content_hash: f5400b49da870989ca3b680c731d21e9cfb1df02
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/fossa.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fossa

Fossa 서비스용 CLI - 종속성 라이센스에 대한 실시간 라이센스 감사, 취약성 검색 및 보고서를 생성.
더 많은 정보: <https://github.com/fossas/fossa-cli>.

- `.fossa.yml` 구성 파일을 초기화:

`fossa init`

- 기본 프로젝트 빌드를 실행:

`fossa build`

- 빌드된 종속성을 분석:

`fossa analyze`

- 보고서 생성:

`fossa report`

- FOSSA 스캔 상태에 대해 현재 개정판을 테스트하고 문제가 발견되면 오류와 함께 종료:

`fossa test`
