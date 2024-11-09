---
layout: page
title: linux/iptables-save (한국어)
description: "`iptables` IPv4 설정 저장."
content_hash: b225b2c46a6f3ace8c1d6d1a47581876493001e3
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/iptables-save.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/iptables-save.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/iptables-save.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># iptables-save

`iptables` IPv4 설정 저장.
IPv6의 경우 `ip6tables-save` 사용.
더 많은 정보: <https://manned.org/iptables-save>.

- `iptables` 설정 출력:

`sudo iptables-save`

- 특정 [t]테이블의 `iptables` 설정 출력:

`sudo iptables-save --table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블</span>

- `iptables` 설정을 [f]파일에 저장:

`sudo iptables-save --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
