---
layout: page
title: linux/nm-online (한국어)
description: "NetworkManager에 네트워크가 연결되어 있는지 확인."
content_hash: 8e65d2ae07a484834f578b056395ffefbf37c9af
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/nm-online.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nm-online.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nm-online

NetworkManager에 네트워크가 연결되어 있는지 확인.
더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nm-online.html>.

- 네트워크가 연결되어 있는지 확인하고 결과를 `stdout`에 출력:

`nm-online`

- 연결을 `n`초 동안 대기 (기본값 30초):

`nm-online --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>
