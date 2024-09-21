---
layout: page
title: common/az-webapp (한국어)
description: "Azure Cloud Services에서 호스팅되는 웹 애플리케이션을 관리."
content_hash: 82451abfa3497a5ed96d3c155a69ecfb08de92e5
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/az-webapp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/az-webapp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/az-webapp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># az webapp

Azure Cloud Services에서 호스팅되는 웹 애플리케이션을 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/webapp>.

- 웹 애플리케이션에 사용 가능한 런타임 나열:

`az webapp list-runtimes --os-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">windows|linux</span>

- 웹 애플리케이션 생성:

`az webapp up --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">위치</span>` --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">런타임</span>

- 모든 웹 애플리케이션 나열:

`az webapp list`

- 특정 웹 애플리케이션 삭제:

`az webapp delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>
