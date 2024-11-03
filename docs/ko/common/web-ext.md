---
layout: page
title: common/web-ext (한국어)
description: "웹 확장 프로그램 개발을 관리하는 명령줄 도구."
content_hash: 632c2995c212b10b479c03556875d092e12fa5fb
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/web-ext.html
    icon: bi bi-globe
tldri18n_status: 2
---
# web-ext

웹 확장 프로그램 개발을 관리하는 명령줄 도구.
더 많은 정보: <https://github.com/mozilla/web-ext>.

- 현재 디렉터리에 있는 웹 확장 프로그램을 Firefox에서 실행:

`web-ext run`

- 특정 디렉터리에서 웹 확장 프로그램을 Firefox에서 실행:

`web-ext run --source-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 자세한 실행 출력 표시:

`web-ext run --verbose`

- Firefox Android에서 웹 확장 프로그램 실행:

`web-ext run --target firefox-android`

- 매니페스트 및 소스 파일의 오류 검사:

`web-ext lint`

- 확장 프로그램 빌드 및 패키징:

`web-ext build`

- 자세한 빌드 출력 표시:

`web-ext build --verbose`

- 자체 호스팅을 위한 패키지 서명:

`web-ext sign --api-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_키</span>` --api-secret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_비밀</span>
