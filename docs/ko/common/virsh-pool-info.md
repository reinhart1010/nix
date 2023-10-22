---
layout: page
title: common/virsh-pool-info (한국어)
description: "가상 머신 스토리지 풀에 대한 정보를 나열합니다."
content_hash: c48cb36ab65d368f142a5cb35c8bd4ff827d0a3c
last_modified_at: 2023-10-22
related_topics:
  - title: English version
    url: /en/common/virsh-pool-info.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-pool-info.html
    icon: bi bi-globe
---
# virsh pool-info

가상 머신 스토리지 풀에 대한 정보를 나열합니다.
같이 보기: `virsh`.
더 많은 정보: <https://manned.org/virsh>.

- 이름 또는 UUID로 지정된 스토리지 풀에 대해 이름, UUID, 상태, 지속성 유형, 자동 시작 상태, 용량, 할당된 공간 및 사용 가능한 공간 나열 (`virsh pool-list`를 사용하여 결정):

`virsh pool-info --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>
