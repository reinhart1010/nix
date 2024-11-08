---
layout: page
title: common/read (한국어)
description: "`stdin`으로부터 데이터를 수신하는 셸 내장 함수."
content_hash: d1dc2a39913dee346f1018797e25a7aaa0efba4a
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/read.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/read.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/read.html
    icon: bi bi-globe
tldri18n_status: 2
---
# read

`stdin`으로부터 데이터를 수신하는 셸 내장 함수.
더 많은 정보: <https://manned.org/read.1p>.

- 키보드로 입력한 데이터를 저장:

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>

- 입력한 각 줄을 배열의 값으로 저장:

`read -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배열</span>

- 읽을 최대 문자 수 지정:

`read -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자_수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>

- 여러 값을 여러 변수에 할당:

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">_ 변수1 _ 변수2</span>` <<< `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"The surname is Bond"</span>

- 백슬래시(\\)를 이스케이프 문자로 사용하지 않음:

`read -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>

- 입력 전에 프롬프트 표시:

`read -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">여기에 입력: </span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>

- 입력한 문자를 표시하지 않음 (비밀 모드):

`read -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>

- `stdin`을 읽고 각 줄에 대해 작업 수행:

`while read line; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo|ls|rm|...</span>` "$line"; done < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/stdin|경로/대상/파일|...</span>
