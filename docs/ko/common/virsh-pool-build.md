---
layout: page
title: common/virsh-pool-build (한국어)
description: "`/etc/libvirt/storage`의 구성 파일에 정의된 대로 가상 머신 스토리지 풀에 대한 기본 스토리지 시스템을 구축합니다."
content_hash: 0b0720ea8bc2b550194ee4e9147594f8ad459f32
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/virsh-pool-build.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-pool-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh pool-build

`/etc/libvirt/storage`의 구성 파일에 정의된 대로 가상 머신 스토리지 풀에 대한 기본 스토리지 시스템을 구축합니다.
같이 보기: `virsh`, `virsh-pool-define-as`, `virsh-pool-start`.
더 많은 정보: <https://manned.org/virsh>.

- 이름 또는 UUID로 지정된 스토리지 풀 구축 (`virsh pool-list`를 사용하여 결정):

`virsh pool-build --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>
