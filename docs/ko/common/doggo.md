---
layout: page
title: common/doggo (한국어)
description: "사람을 위한 DNS 클라이언트."
content_hash: c22c8cdc65b80893f34f08b7819542a5e7a310eb
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/doggo.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/doggo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doggo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doggo

사람을 위한 DNS 클라이언트.
Golang으로 작성됨.
더 많은 정보: <https://github.com/mr-karan/doggo>.

- 간단한 DNS 조회를 수행:

`doggo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 특정 네임서버를 사용하여 MX 레코드를 쿼리:

`doggo MX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codeberg.org</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.2</span>

- HTTPS를 통해 DNS 사용:

`doggo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://dns.quad9.net/dns-query</span>

- JSON 형식으로 출력:

`doggo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --json | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.responses[0].answers[].address</span>`'`

- 역방향 DNS 조회를 수행:

`doggo --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.4.4</span>` --short`
