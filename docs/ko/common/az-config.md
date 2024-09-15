---
layout: page
title: common/az-config (한국어)
description: "Azure CLI 구성을 관리."
content_hash: a8d663d4e5c7cd00ab7d593b755c58a514565ee4
last_modified_at: 2024-09-15
related_topics:
  - title: Deutsch version
    url: /de/common/az-config.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/az-config.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/az-config.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/az-config.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># az config

Azure CLI 구성을 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/config>.

- 모든 구성 설정을 출력:

`az config get`

- 특정 섹션에 대한 구성 설정 출력:

`az config get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">섹션_이름</span>

- 구성을 설정:

`az config set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_이름</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 구성 설정을 해제:

`az config unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_이름</span>
