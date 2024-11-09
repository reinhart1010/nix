---
layout: page
title: linux/dget (한국어)
description: "Debian 패키지 다운로드."
content_hash: 643180ffb1ab64dc8807cb7e9e0bd0c1a27d310e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/dget.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dget

Debian 패키지 다운로드.
더 많은 정보: <https://manned.org/dget.1>.

- 바이너리 패키지 다운로드:

`dget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- `.dsc` 파일에서 패키지 소스를 다운로드하고 추출:

`dget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc</span>

- `.dsc` 파일에서 패키지 소스 tarball을 다운로드하지만 추출하지 않음:

`dget -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc</span>
