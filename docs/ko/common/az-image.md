---
layout: page
title: common/az-image (한국어)
description: "Azure에서 사용자 지정 가상 머신 이미지를 관리."
content_hash: ac17a202b260f7f7721d940aeb95c776e309c5e1
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/az-image.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az image

Azure에서 사용자 지정 가상 머신 이미지를 관리.
`azure-cli` (`az`라고도 함)의 일부.
더 많은 정보: <https://learn.microsoft.com/cli/azure/image>.

- 리소스 그룹 아래에 사용자 정의 이미지를 나열:

`az image list --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>

- 관리 디스크 또는 스냅샷에서 사용자 지정 이미지를 생성:

`az image create --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --os-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">windows|linux</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os_디스크_소스</span>

- 사용자 정의 이미지 삭제:

`az image delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>

- 사용자 정의 이미지의 세부정보 표시:

`az image show --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>

- 사용자 정의 이미지 업데이트:

`az image update --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>` --set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">property=value</span>
