---
layout: page
title: common/az-vm (한국어)
description: "Azure에서 가상 머신을 관리."
content_hash: bc14c2d2ec32a04e088f5a7823b5cb2f992e17a6
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/az-vm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/az-vm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az vm

Azure에서 가상 머신을 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/vm>.

- 사용 가능한 가상 머신의 세부 정보 나열:

`az vm list`

- 기본 Ubuntu 이미지를 사용하여 가상 머신을 생성하고 SSH 키를 생성:

`az vm create --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스그룹</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상머신_이름</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UbuntuLTS</span>` --admin-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">azureuser</span>` --generate-ssh-keys`

- 가상 머신 정지:

`az vm stop --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스그룹</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상머신_이름</span>

- 가상 머신 할당 해제:

`az vm deallocate --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스그룹</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상머신_이름</span>

- 가상 머신 시작:

`az vm start --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스그룹</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- 가상 머신 재시작:

`az vm restart --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스그룹</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상머신_이름</span>

- Azure Marketplace에서 사용할 수 있는 VM 이미지를 나열:

`az vm image list`
