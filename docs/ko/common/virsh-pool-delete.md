---
layout: page
title: common/virsh-pool-delete (한국어)
description: "비활성 가상 머신 스토리지 풀의 기본 스토리지 시스템 삭제."
content_hash: f4d660e36737de0b42af83bce6193ef4e90eedc1
last_modified_at: 2023-10-22
related_topics:
  - title: English version
    url: /en/common/virsh-pool-delete.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-pool-delete.html
    icon: bi bi-globe
---
# virsh pool-delete

비활성 가상 머신 스토리지 풀의 기본 스토리지 시스템 삭제.
같이 보기: `virsh`, `virsh-pool-destroy`, `virsh-pool-undefine`.
더 많은 정보: <https://manned.org/virsh>.

- 이름 또는 UUID로 지정된 스토리지 풀에 대한 기본 스토리지 시스템을 삭제 (`virsh pool-list`을 사용하여 결정):

`virsh pool-delete --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>
