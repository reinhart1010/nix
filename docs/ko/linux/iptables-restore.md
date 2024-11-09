---
layout: page
title: linux/iptables-restore (한국어)
description: "`iptables` IPv4 구성을 복원합니다."
content_hash: 63aaeb8ffa3337936ff5b7ca22e182e9deded755
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/iptables-restore.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/iptables-restore.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/iptables-restore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># iptables-restore

`iptables` IPv4 구성을 복원합니다.
IPv6에 대해 동일한 작업을 수행하려면 `ip6tables-restore`를 사용합니다.
더 많은 정보: <https://manned.org/iptables-restore>.

- 파일에서 `iptables` 구성 복원:

`sudo iptables-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
