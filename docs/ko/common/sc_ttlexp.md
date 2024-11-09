---
layout: page
title: common/sc_ttlexp (한국어)
description: "`warts` 파일에서 ICMP TTL 만료 메시지의 소스 주소를 덤프."
content_hash: cd28d53fa742dd39a926981d8cd95d4d4bef0adf
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/sc_ttlexp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/sc_ttlexp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sc_ttlexp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sc_ttlexp

`warts` 파일에서 ICMP TTL 만료 메시지의 소스 주소를 덤프.
더 많은 정보: <https://www.caida.org/catalog/software/scamper/>.

- `warts` 파일에서 ICMP TTL 만료 메시지의 소스 주소를 순차적으로 출력:

`sc_ttlexp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.warts 경로/대상/파일2.warts ...</span>
