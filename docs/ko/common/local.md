---
layout: page
title: common/local (한국어)
description: "로컬 변수를 선언하고 속성을 부여합니다."
content_hash: d7487a0becec8901e8c007f68089ad13d0d3ab4e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/local.html
    icon: bi bi-globe
tldri18n_status: 2
---
# local

로컬 변수를 선언하고 속성을 부여합니다.
더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- 지정된 값으로 문자열 변수 선언:

`local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 지정된 값으로 정수 변수 선언:

`local -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 지정된 값으로 배열 변수 선언:

`local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_a 항목_b 항목_c</span>`)`

- 지정된 값으로 연관 배열 변수 선언:

`local -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[키_a]=항목_a [키_b]=항목_b [키_c]=항목_c</span>`)`

- 지정된 값으로 읽기 전용 변수 선언:

`local -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`
