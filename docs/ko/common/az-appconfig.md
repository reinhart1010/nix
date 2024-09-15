---
layout: page
title: common/az-appconfig (한국어)
description: "Azure에서 앱 구성을 관리."
content_hash: feecdcb321fcd361447902cc9a58fad463700977
last_modified_at: 2024-09-15
related_topics:
  - title: English version
    url: /en/common/az-appconfig.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/az-appconfig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/az-appconfig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># az appconfig

Azure에서 앱 구성을 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/appconfig>.

- 앱 구성 만들기:

`az appconfig create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>` --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">위치</span>

- 특정 앱 구성 삭제:

`az appconfig delete --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스그룹_이름</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱구성파일_이름</span>

- 현재 구독 아래의 모든 앱 구성을 나열:

`az appconfig list`

- 특정 리소스 그룹 아래 모든 앱 구성을 나열:

`az appconfig list --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스그룹_이름</span>

- 앱 구성의 속성 표시:

`az appconfig show --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱구성파일_이름</span>

- 특정 앱 구성 업데이트:

`az appconfig update --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스그룹_이름</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱구성파일_이름</span>
