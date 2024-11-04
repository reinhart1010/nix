---
layout: page
title: windows/ipconfig (한국어)
description: "Windows의 네트워크 구성을 표시하고 관리합니다."
content_hash: a91457b7d2901fb826af07ca9ba0cf6746f28bc9
last_modified_at: 2024-11-04
related_topics:
  - title: Deutsch version
    url: /de/windows/ipconfig.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/ipconfig.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/ipconfig.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/ipconfig.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/ipconfig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/ipconfig.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/ipconfig.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/ipconfig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/ipconfig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ipconfig

Windows의 네트워크 구성을 표시하고 관리합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- 모든 네트워크 어댑터 표시:

`ipconfig`

- 네트워크 어댑터의 자세한 목록을 표시:

`ipconfig /all`

- 네트워크 어댑터의 IP 주소 갱신:

`ipconfig /renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">어댑터</span>

- 네트워크 어댑터의 IP 주소 해제:

`ipconfig /release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">어댑터</span>

- 로컬 DNS 캐시 표시:

`ipconfig /displaydns`

- 로컬 DNS 캐시의 모든 데이터 제거:

`ipconfig /flushdns`
