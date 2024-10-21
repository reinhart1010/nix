---
layout: page
title: common/az-logicapp (한국어)
description: "Azure Cloud Services에서 논리 앱을 관리."
content_hash: da9a0d9be6d64f5152cbe293f98e0c28fad50bbb
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/az-logicapp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az logicapp

Azure Cloud Services에서 논리 앱을 관리.
`azure-cli` (`az`라고도 함)의 일부.
더 많은 정보: <https://learn.microsoft.com/cli/azure/logicapp>.

- 논리 앱 만들기:

`az logicapp create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>` --storage-account `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토리지_계정</span>

- 논리 앱 삭제:

`az logicapp delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>

- 논리 앱 나열:

`az logicapp list --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>

- 논리 앱을 다시 시작:

`az logicapp restart --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>

- 논리 앱을 시작:

`az logicapp start --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>

- 논리 앱을 중지:

`az logicapp stop --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>
