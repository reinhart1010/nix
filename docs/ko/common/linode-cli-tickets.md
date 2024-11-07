---
layout: page
title: common/linode-cli-tickets (한국어)
description: "Linode 지원 티켓 관리."
content_hash: fed8ee968d119b27efbfffd577cf9b98b01e54a7
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/linode-cli-tickets.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/linode-cli-tickets.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># linode-cli tickets

Linode 지원 티켓 관리.
같이 보기: `linode-cli`.
더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-account-management>.

- 지원 티켓 목록 보기:

`linode-cli tickets list`

- 새 티켓 열기:

`linode-cli tickets create --summary "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">티켓에 대한 요약 또는 간단한 제목</span>`" --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문제에 대한 자세한 설명</span>`"`

- 티켓에 대한 답변 목록 보기:

`linode-cli tickets replies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">티켓_ID</span>

- 특정 티켓에 답장하기:

`linode-cli tickets reply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">티켓_ID</span>` --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">답변 내용</span>`"`
