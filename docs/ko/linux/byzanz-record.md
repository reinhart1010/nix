---
layout: page
title: linux/byzanz-record (한국어)
description: "화면을 녹화합니다."
content_hash: 49197a3743a732e37d44dd34c426b8a394ca066d
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/byzanz-record.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/byzanz-record.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># byzanz-record

화면을 녹화합니다.
더 많은 정보: <https://manned.org/byzanz-record>.

- 화면을 녹화하고 파일에 기록 (기본적으로 `byzanz-record`는 10초만 녹화합니다):

`byzanz-record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.[byzanz|flv|gif|ogg|ogv|webm]</span>

- 녹화 중 및 녹화 후 정보를 표시:

`byzanz-record --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.[byzanz|flv|gif|ogg|ogv|webm]</span>

- 화면을 1분 동안 녹화:

`byzanz-record --duration 60 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.[byzanz|flv|gif|ogg|ogv|webm]</span>

- 녹화를 10초 지연 후 시작:

`byzanz-record --delay 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.[byzanz|flv|gif|ogg|ogv|webm]</span>
