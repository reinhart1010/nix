---
layout: page
title: common/pio-test (한국어)
description: "PlatformIO 프로젝트에서 로컬 테스트 실행."
content_hash: 61d953b8a99245b2118730edb88b4c5229b4ece9
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pio-test.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-test.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio test

PlatformIO 프로젝트에서 로컬 테스트 실행.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/cmd_test.html>.

- 현재 PlatformIO 프로젝트의 모든 환경에서 모든 테스트 실행:

`pio test`

- 특정 환경에서만 테스트 실행:

`pio test --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경1</span>` --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경2</span>

- 이름이 특정 글로브 패턴과 일치하는 테스트만 실행:

`pio test --filter "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>`"`

- 이름이 특정 글로브 패턴과 일치하는 테스트를 무시:

`pio test --ignore "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>`"`

- 펌웨어 업로드를 위한 포트 지정:

`pio test --upload-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">업로드_포트</span>

- 테스트 실행을 위한 사용자 정의 설정 파일 지정:

`pio test --project-conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/platformio.ini</span>
