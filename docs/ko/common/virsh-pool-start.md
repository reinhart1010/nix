---
layout: page
title: common/virsh-pool-start (한국어)
description: "이전에 구성되었지만 비활성화된 가상 머신 스토리지 풀 시작."
content_hash: 332c5947c5421b4b7aa151bc1b1b01c070dc0574
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/virsh-pool-start.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-pool-start.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh pool-start

이전에 구성되었지만 비활성화된 가상 머신 스토리지 풀 시작.
같이 보기: `virsh`, `virsh-pool-define-as`, `virsh-pool-destroy`.
더 많은 정보: <https://manned.org/virsh>.

- 이름 또는 UUID로 지정된 스토리지 풀을 시작하고 (`virsh pool-list`를 사용하여 결정) 기본 스토리지 시스템이 없으면 생성:

`virsh pool-start --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>` --build`
