---
layout: page
title: common/az-apim (한국어)
description: "Azure API Management 서비스를 관리."
content_hash: 8ec7030ff75b702a779aa334ff5700bbe224bf51
last_modified_at: 2024-09-16
related_topics:
  - title: English version
    url: /en/common/az-apim.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/az-apim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az apim

Azure API Management 서비스를 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/apim>.

- 리소스 그룹 내 API Management 서비스를 나열:

`az apim list --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>

- API Management 서비스 인스턴스 생성:

`az apim create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>` --publisher-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일</span>` --publisher-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- API Management 서비스 삭제:

`az apim delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>

- API Management 서비스 인스턴스의 세부정보 표시:

`az apim show --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>

- API Management 서비스 인스턴스 업데이트:

`az apim update --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>
