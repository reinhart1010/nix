---
layout: page
title: common/linode-cli-domains (한국어)
description: "Linode 도메인 및 DNS 구성 관리."
content_hash: 47c604e1bceac3a11d0a2001f1299d607ffe943d
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/linode-cli-domains.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/linode-cli-domains.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/linode-cli-domains.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># linode-cli domains

Linode 도메인 및 DNS 구성 관리.
같이 보기: `linode-cli`.
더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-the-dns-manager>.

- 관리되는 모든 도메인 나열:

`linode-cli domains list`

- 새 관리 도메인 생성:

`linode-cli domains create --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master|slave</span>` --soa-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일</span>

- 특정 도메인의 세부 정보 보기:

`linode-cli domains view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_ID</span>

- 관리 도메인 삭제:

`linode-cli domains delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_ID</span>

- 특정 도메인의 레코드 나열:

`linode-cli domains records-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_ID</span>

- 도메인에 DNS 레코드 추가:

`linode-cli domains records-create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_ID</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|AAAA|CNAME|MX|...</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서브도메인</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_값</span>

- 도메인의 DNS 레코드 업데이트:

`linode-cli domains records-update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레코드_ID</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_대상_값</span>

- 도메인에서 DNS 레코드 삭제:

`linode-cli domains records-delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레코드_ID</span>
