---
layout: page
title: common/typeset (한국어)
description: "변수를 선언하고 속성을 부여합니다."
content_hash: cde2bdf1609e0d3ced2514daf5f2772b20945abd
last_modified_at: 2024-12-22
related_topics:
  - title: English version
    url: /en/common/typeset.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># typeset

변수를 선언하고 속성을 부여합니다.
더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- 지정된 값으로 문자열 변수 선언:

`typeset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 지정된 값으로 정수 변수 선언:

`typeset -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 지정된 값으로 배열 변수 선언:

`typeset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_a 항목_b 항목_c</span>`)`

- 지정된 값으로 연관 배열 변수 선언:

`typeset -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[키_a]=항목_a [키_b]=항목_b [키_c]=항목_c</span>`)`

- 지정된 값으로 읽기 전용 변수 선언:

`typeset -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 함수 내에서 지정된 값으로 전역 변수 선언:

`typeset -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`
