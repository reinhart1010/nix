---
layout: page
title: osx/wc (한국어)
description: "줄, 단어 또는 바이트 수를 계산."
content_hash: 6f2ffe38cc0fd3cb4382164eefaf335fe34c94d5
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/wc.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/wc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/wc.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/wc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wc

줄, 단어 또는 바이트 수를 계산.
더 많은 정보: <https://keith.github.io/xcode-man-pages/wc.1.html>.

- [f]파일의 줄 수 계산:

`wc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- [f]파일의 단어 수 계산:

`wc -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- [f]파일의 문자 수(바이트) 계산:

`wc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 멀티바이트 문자 집합을 고려하여 [f]파일의 문자 수 계산:

`wc -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`을 사용하여 순서대로 줄, 단어 및 문자 수(바이트) 계산:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`
