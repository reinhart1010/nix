---
layout: page
title: common/az-acr (한국어)
description: "Azure Container Registries를 사용해 프라이빗 레지스트리를 관리."
content_hash: e7c229a0987e6354a2486fad98a18fc96aee0416
last_modified_at: 2024-09-16
related_topics:
  - title: English version
    url: /en/common/az-acr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az acr

Azure Container Registries를 사용해 프라이빗 레지스트리를 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/acr>.

- 관리형 컨테이너 레지스트리를 생성:

`az acr create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>` --sku `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sku</span>

- 레지스트리에 로그인:

`az acr login --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_이름</span>

- ACR용 로컬 이미지에 태그를 지정:

`docker tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_이름</span>`.azurecr.io/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 이미지를 레지스트리에 푸시:

`docker push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_이름</span>`.azurecr.io/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 레지스트리에서 이미지를 가져옴:

`docker pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_이름</span>`.azurecr.io/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 레지스트리에서 이미지 삭제:

`az acr repository delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_이름</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 관리형 컨테이너 레지스트리를 삭제:

`az acr delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>` --yes`

- 레지스트리 내의 이미지 목록 나열:

`az acr repository list --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_이름</span>` --output table`
