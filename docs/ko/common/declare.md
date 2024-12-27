---
layout: page
title: common/declare (한국어)
description: "변수를 선언하고 속성을 부여."
content_hash: 6e3f8e7bfa6e58cd0752ff68d205ae2cd862bc70
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/common/declare.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># declare

변수를 선언하고 속성을 부여.
더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- 지정된 값을 사용하여 문자열 변수를 선언:

`declare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 지정된 값을 가진 정수 변수를 선언:

`declare -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 지정된 값을 사용하여 배열 변수를 선언:

`declare -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_a 항목_b 항목_c</span>`)`

- 지정된 값을 사용하여 연관 배열 변수를 선언:

`declare -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[키_a]=항목_a [키_b]=항목_b [키_c]=항목_c</span>`)`

- 지정된 값을 사용해 읽기 전용 문자열 변수를 선언:

`declare -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 지정된 값을 사용해 함수 내에서 전역 변수를 선언:

`declare -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`
