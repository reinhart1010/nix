---
layout: page
title: common/shfmt (한국어)
description: "셸 파서, 포매터 및 인터프리터."
content_hash: d2c47f27f2c341792c3098eb72245ec69be8057c
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/shfmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shfmt

셸 파서, 포매터 및 인터프리터.
더 많은 정보: <https://pkg.go.dev/mvdan.cc/sh>.

- 셸 스크립트를 포맷된 버전으로 출력:

`shfmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 포맷되지 않은 파일 목록:

`shfmt --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 결과를 터미널에 출력하지 않고 파일에 작성:

`shfmt --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 코드 단순화, 불필요한 구문 제거 (예: 표현식에서 변수의 "$" 제거):

`shfmt --simplify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
