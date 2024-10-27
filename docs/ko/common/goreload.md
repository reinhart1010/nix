---
layout: page
title: common/goreload (한국어)
description: "Go 프로그램용 라이브 리로드 유틸리티."
content_hash: 0efa786ff8a469173e43218d90029e369e4fda6e
last_modified_at: 2024-10-27
related_topics:
  - title: English version
    url: /en/common/goreload.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/goreload.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># goreload

Go 프로그램용 라이브 리로드 유틸리티.
더 많은 정보: <https://github.com/acoshift/goreload>.

- 바이너리 파일 보기 (기본값은 `.goreload`):

`goreload -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.go</span>

- 사용자 정의 로그 접두사를 설정 (기본값은 `goreload`):

`goreload --logPrefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.go</span>

- 파일이 변경될 때마다 다시 로드:

`goreload --all`
