---
layout: page
title: common/whois (한국어)
description: "WHOIS (RFC 3912) 프로토콜을 위한 명령줄 클라이언트."
content_hash: 8ec88ae946613e4264b60ff0f24e4d4d6e62028c
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/whois.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/whois.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/whois.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/whois.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/whois.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># whois

WHOIS (RFC 3912) 프로토콜을 위한 명령줄 클라이언트.
더 많은 정보: <https://github.com/rfc1036/whois>.

- 도메인 이름에 대한 정보 조회:

`whois `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- IP 주소에 대한 정보 조회:

`whois `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- IP 주소에 대한 abuse 연락처 조회:

`whois -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>
