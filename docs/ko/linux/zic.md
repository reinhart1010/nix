---
layout: page
title: linux/zic (한국어)
description: "시간대 정보를 바이너리 파일로 컴파일."
content_hash: 15a8554100282810b0b2ad61d3ea5035175c9e73
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/zic.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/zic.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zic

시간대 정보를 바이너리 파일로 컴파일.
더 많은 정보: <https://manned.org/zic>.

- 디렉터리에서 시간대 파일을 컴파일:

`zic -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 파일을 컴파일하는 동안 경고 보고:

`zic -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`.infile`
