---
layout: page
title: common/virsh-pool-destroy (한국어)
description: "활성 가상 머신 스토리지 풀 중지."
content_hash: 84c40290879477b3851c9113c21ae0db64668f55
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/virsh-pool-destroy.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-pool-destroy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh pool-destroy

활성 가상 머신 스토리지 풀 중지.
같이 보기: `virsh`, `virsh-pool-delete`.
더 많은 정보: <https://manned.org/virsh>.

- 이름 또는 UUID로 지정된 스토리지 풀 중지 (`virsh pool-list`를 사용하여 결정):

`virsh pool-destroy --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>
