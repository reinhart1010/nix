---
layout: page
title: common/virsh-pool-autostart (한국어)
description: "가상 머신 스토리지 풀에 대한 자동 시작 활성화 또는 비활성화."
content_hash: 666773c8a6f42ff531a3a31731220a77668af64a
last_modified_at: 2023-10-22
related_topics:
  - title: English version
    url: /en/common/virsh-pool-autostart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-pool-autostart.html
    icon: bi bi-globe
---
# virsh pool-autostart

가상 머신 스토리지 풀에 대한 자동 시작 활성화 또는 비활성화.
같이 보기: `virsh`.
더 많은 정보: <https://manned.org/virsh>.

- 이름 또는 UUID로 지정된 스토리지 풀에 대한 자동 시작 활성화 (`virsh pool-list`를 사용하여 결정):

`virsh pool-autostart --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>

- 이름 또는 UUID로 지정된 스토리지 풀에 대한 자동 시작 비활성화:

`virsh pool-autostart --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>` --disable`
