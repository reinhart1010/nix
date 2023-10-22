---
layout: page
title: common/virsh-pool-undefine (한국어)
description: "중지된 가상 머신 스토리지 풀에 대한 `/etc/libvirt/storage`에서 구성 파일을 삭제합니다."
content_hash: b44913f6563290f9714e1d30ad91d28eb8d7473a
last_modified_at: 2023-10-22
related_topics:
  - title: English version
    url: /en/common/virsh-pool-undefine.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-pool-undefine.html
    icon: bi bi-globe
---
# virsh pool-undefine

중지된 가상 머신 스토리지 풀에 대한 `/etc/libvirt/storage`에서 구성 파일을 삭제합니다.
같이 보기: `virsh`, `virsh-pool-destroy`.
더 많은 정보: <https://manned.org/virsh>.

- 스토리지 풀에 지정된 이름 또는 UUID에 대한 구성을 삭제 (`virsh pool-list`를 사용하여 결정):

`virsh pool-undefine --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>
