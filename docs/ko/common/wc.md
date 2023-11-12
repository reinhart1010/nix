---
layout: page
title: common/wc (한국어)
description: "줄 단어 및 바이트 수 계산."
content_hash: 149fc64647ffa43f7bc5370214891292d31e3f5a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/wc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/wc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/wc.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/wc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/wc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wc

줄 단어 및 바이트 수 계산.
더 많은 정보: <https://www.gnu.org/software/coreutils/wc>.

- 파일의 모든 줄 수 계산:

`wc --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 모든 단어 수 계산:

`wc --words `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 모든 바이트 수 계산:

`wc --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 모든 문자 수 계산(멀티바이트 문자 고려):

`wc --chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`의 모든 줄, 단어 및 바이트 수를 계산:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`

- 가장 긴 줄의 길이를 문자 수로 계산:

`wc --max-line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
