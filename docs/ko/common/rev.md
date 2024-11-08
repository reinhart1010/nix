---
layout: page
title: common/rev (한국어)
description: "텍스트 라인이나 파일을 뒤집습니다."
content_hash: 40f94c2eaca2ee324ddc6a8337403cb7e6e57473
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/common/rev.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/rev.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/rev.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rev

텍스트 라인이나 파일을 뒤집습니다.
더 많은 정보: <https://manned.org/rev>.

- 터미널에 입력한 텍스트 뒤집기:

`rev`

- 문자열 "hello" 뒤집기:

`echo "hello" | rev`

- 전체 파일을 뒤집어 `stdout`에 출력:

`rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 줄 구분자로 '\0'을 사용 (제로 종료):

`rev -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 도움말 표시:

`rev -h`

- 버전 표시:

`rev -V`
