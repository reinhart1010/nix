---
layout: page
title: common/virsh-domblklist (한국어)
description: "가상 머신과 연결된 블록 장치에 대한 정보 나열."
content_hash: 9fb8643651bb37838eaf3022f9a26900e07fa11c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/virsh-domblklist.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-domblklist.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh-domblklist

가상 머신과 연결된 블록 장치에 대한 정보 나열.
같이 보기: `virsh`.
더 많은 정보: <https://manned.org/virsh>.

- 블록 장치의 대상 이름 및 소스 경로 나열:

`virsh domblklist --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상머신_이름</span>

- 디스크 유형, 장치 값, 대상 이름 및 소스 경로 나열:

`virsh domblklist --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상머신_이름</span>` --details`
