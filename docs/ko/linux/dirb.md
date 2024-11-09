---
layout: page
title: linux/dirb (한국어)
description: "HTTP 기반 웹 서버의 디렉토리와 파일을 스캔합니다."
content_hash: 3cf7203ba8ae8fadc5a4c40cc06dbb9bc3588ba0
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/dirb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dirb

HTTP 기반 웹 서버의 디렉토리와 파일을 스캔합니다.
더 많은 정보: <https://dirb.sourceforge.net>.

- 기본 단어 목록을 사용하여 웹 서버 스캔:

`dirb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>

- 사용자 정의 단어 목록을 사용하여 웹 서버 스캔:

`dirb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록.txt</span>

- 비재귀적으로 웹 서버 스캔:

`dirb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>` -r`

- 지정된 사용자 에이전트와 쿠키를 사용하여 웹 서버 스캔:

`dirb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_에이전트_스트링</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿠키_스트링</span>
