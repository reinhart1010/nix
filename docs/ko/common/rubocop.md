---
layout: page
title: common/rubocop (한국어)
description: "Ruby 파일을 린트합니다."
content_hash: 6bc5347af3133254e5d671c81654934b72470bab
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rubocop.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/rubocop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/rubocop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rubocop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rubocop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rubocop

Ruby 파일을 린트합니다.
더 많은 정보: <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- 현재 디렉토리의 모든 파일 확인(하위 디렉토리 포함):

`rubocop`

- 하나 이상의 특정 파일 또는 디렉토리 확인:

`rubocop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>

- 출력 결과를 파일에 저장:

`rubocop --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- cop(린터 규칙) 목록 보기:

`rubocop --show-cops`

- 특정 cop 제외:

`rubocop --except `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop1 cop2 ...</span>

- 지정된 cop만 실행:

`rubocop --only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop1 cop2 ...</span>

- 파일 자동 수정(실험적 기능):

`rubocop --auto-correct`
