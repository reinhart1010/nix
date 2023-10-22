---
layout: page
title: common/virsh-pool-define-as (한국어)
description: "제공된 인수를 사용하여 영구 가상 머신 스토리지 풀에 대한 `/etc/libvirt/storage`에 구성 파일을 생성합니다."
content_hash: 3f9af1413453cdff2d9ba481ab3a2a701134df00
last_modified_at: 2023-10-22
related_topics:
  - title: English version
    url: /en/common/virsh-pool-define-as.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-pool-define-as.html
    icon: bi bi-globe
---
# virsh pool-define-as

제공된 인수를 사용하여 영구 가상 머신 스토리지 풀에 대한 `/etc/libvirt/storage`에 구성 파일을 생성합니다.
같이 보기: `virsh`, `virsh-pool-build`, `virsh-pool-start`.
더 많은 정보: <https://manned.org/virsh>.

- 기본 스토리지 시스템으로 `/var/vms`를 사용하여 pool_name이라는 스토리지 풀에 대한 구성 파일을 생성:

`virsh pool-define-as --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/vms</span>
