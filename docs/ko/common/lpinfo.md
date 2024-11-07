---
layout: page
title: common/lpinfo (한국어)
description: "CUPS 프린트 서버의 연결된 프린터 및 설치된 드라이버 나열."
content_hash: cd5e33c45a7af1b05033f68255a7dc37d60d31ae
last_modified_at: 2024-11-07
related_topics:
  - title: Deutsch version
    url: /de/common/lpinfo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/lpinfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lpinfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lpinfo

CUPS 프린트 서버의 연결된 프린터 및 설치된 드라이버 나열.
더 많은 정보: <https://openprinting.github.io/cups/doc/man-lpinfo.html>.

- 현재 연결된 모든 프린터 나열:

`lpinfo -v`

- 현재 설치된 모든 프린터 드라이버 나열:

`lpinfo -m`

- 제조사 및 모델로 설치된 프린터 드라이버 검색:

`lpinfo --make-and-model "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터_모델</span>`" -m`
