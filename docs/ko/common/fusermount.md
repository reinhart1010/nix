---
layout: page
title: common/fusermount (한국어)
description: "FUSE 파일시스템 마운트 및 마운트 해제."
content_hash: b10a2026aecf2494cecf8c279fcff3c098602f7d
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fusermount.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fusermount.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fusermount

FUSE 파일시스템 마운트 및 마운트 해제.
더 많은 정보: <https://manned.org/fusermount>.

- FUSE 파일시스템 마운트 해제:

`fusermount -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>

- FUSE 파일시스템이 사용되지 않는 즉시 마운트를 해제:

`fusermount -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>

- 버전 정보 표시:

`fusermount --version`
