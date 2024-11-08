---
layout: page
title: linux/dget (한국어)
description: "Debian 패키지 다운로드."
content_hash: 643180ffb1ab64dc8807cb7e9e0bd0c1a27d310e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dget.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dget.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dget

Debian 패키지 다운로드.
더 많은 정보: <https://manned.org/dget.1>.

- 바이너리 패키지 다운로드:

`dget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- `.dsc` 파일에서 패키지 소스를 다운로드하고 추출:

`dget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc</span>

- `.dsc` 파일에서 패키지 소스 tarball을 다운로드하지만 추출하지 않음:

`dget -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc</span>
