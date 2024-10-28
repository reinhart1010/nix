---
layout: page
title: common/goreload (한국어)
description: "Go 프로그램용 라이브 리로드 유틸리티."
content_hash: 0efa786ff8a469173e43218d90029e369e4fda6e
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/common/goreload.html
    icon: bi bi-globe
tldri18n_status: 2
---
# goreload

Go 프로그램용 라이브 리로드 유틸리티.
더 많은 정보: <https://github.com/acoshift/goreload>.

- 바이너리 파일 보기 (기본값은 `.goreload`):

`goreload -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.go</span>

- 사용자 정의 로그 접두사를 설정 (기본값은 `goreload`):

`goreload --logPrefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.go</span>

- 파일이 변경될 때마다 다시 로드:

`goreload --all`
