---
layout: page
title: common/linode-cli-events (한국어)
description: "Linode 이벤트 관리."
content_hash: 3203f8f7bb7389aef20f253c78cf14624d4e974b
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/linode-cli-events.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/linode-cli-events.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># linode-cli events

Linode 이벤트 관리.
같이 보기: `linode-cli`.
더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-viewing-events>.

- 계정의 이벤트 목록 보기:

`linode-cli events list`

- 특정 이벤트에 대한 세부 정보 보기:

`linode-cli events view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이벤트_ID</span>

- 이벤트를 읽은 것으로 표시:

`linode-cli events mark-read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이벤트_ID</span>
