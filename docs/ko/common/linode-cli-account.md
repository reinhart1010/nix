---
layout: page
title: common/linode-cli-account (한국어)
description: "Linode 계정 관리."
content_hash: 05b85be582329c643349a9de1124df7f748d0e77
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/linode-cli-account.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/linode-cli-account.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/linode-cli-account.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># linode-cli account

Linode 계정 관리.
같이 보기: `linode-cli`.
더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-account-management>.

- 계정 보기:

`linode-cli account view`

- 계정 설정 보기:

`linode-cli account settings`

- 결제하기:

`linode-cli account payment-create --cvv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CVV</span>` --usd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">달러_금액</span>

- 계정 알림 보기:

`linode-cli account notifications-list`
