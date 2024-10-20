---
layout: page
title: common/flarectl (한국어)
description: "Cloudflare 공식 CLI."
content_hash: 449b4ff6c986a17d4f3797dc3cb77a95fef96853
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/flarectl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/flarectl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># flarectl

Cloudflare 공식 CLI.
더 많은 정보: <https://github.com/cloudflare/cloudflare-go/blob/master/cmd/flarectl/README.md>.

- 특정 IP 차단:

`flarectl firewall rules create --zone="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`" --value="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>`" --mode="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">block</span>`" --notes="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Block bad actor</span>`"`

- DNS 레코드 추가:

`flarectl dns create --zone="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`" --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app</span>`" --type="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CNAME</span>`" --content="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myapp.herokuapp.com</span>`" --proxy`

- 모든 Cloudflare IPv4/IPv6 범위 나열:

`flarectl ips --ip-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ipv4|ipv6|all</span>

- `domains.txt`의 이름을 사용하여 자동으로 많은 새 Cloudflare 영역을 생성:

`for domain in $(cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domains.txt</span>`); do flarectl zone info --zone=$domain; done`

- 모든 방화벽 규칙을 나열:

`flarectl firewall rules list`
