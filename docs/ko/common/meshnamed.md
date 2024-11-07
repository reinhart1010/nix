---
layout: page
title: common/meshnamed (한국어)
description: "IPv6 메쉬 네트워크를 위한 분산 네이밍 시스템."
content_hash: e739d0476107184bc331b4e01860a14ff316a617
last_modified_at: 2024-11-07
related_topics:
  - title: Deutsch version
    url: /de/common/meshnamed.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/meshnamed.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/meshnamed.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># meshnamed

IPv6 메쉬 네트워크를 위한 분산 네이밍 시스템.
더 많은 정보: <https://github.com/zhoreeq/meshname/>.

- 로컬 메쉬네임 DNS 서버 시작:

`meshnamed`

- IPv6 주소를 메쉬네임으로 변환:

`meshnamed -getname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200:6fc8:9220:f400:5cc2:305a:4ac6:967e</span>

- 메쉬네임을 IPv6 주소로 변환:

`meshnamed -getip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aiag7sesed2aaxgcgbnevruwpy</span>
