---
layout: page
title: common/bear (한국어)
description: "`clang` 도구용 컴파일 데이터베이스를 생성하는 도구."
content_hash: 27c73a3fef1057dfbad7d22c9b992f86790acb86
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/bear.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bear

`clang` 도구용 컴파일 데이터베이스를 생성하는 도구.
더 많은 정보: <https://github.com/rizsotto/Bear>.

- 빌드 명령을 실행하여 `compile_commands.json`을 생성:

`bear -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- 사용자 정의 출력 파일 이름으로 컴파일 데이터베이스 생성:

`bear --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/컴파일_명령어.json</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- 기존 `compile_commands.json` 파일에 결과를 추가:

`bear --append -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- 자세한 출력을 얻으려면, 상세 모드로 실행:

`bear --verbose -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- `bear`가 명령 차단을 위해 사전 로드 방법을 사용하도록 강제:

`bear --force-preload -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>
