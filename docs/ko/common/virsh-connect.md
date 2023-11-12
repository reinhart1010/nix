---
layout: page
title: common/virsh-connect (한국어)
description: "가상 머신 하이퍼바이저에 연결합니다."
content_hash: 47cc1ca8419efa77f2ade5629e500df5e42ddfb3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/virsh-connect.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-connect.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh-connect

가상 머신 하이퍼바이저에 연결합니다.
같이 보기: `virsh`.
더 많은 정보: <https://manned.org/virsh>.

- 기본 하이퍼바이저에 연결:

`virsh connect`

- 로컬 QEMU/KVM 하이퍼바이저에 루트로 연결:

`virsh connect qemu:///system`

- 하이퍼바이저의 새 인스턴스를 시작하고, 로컬 사용자로 연결:

`virsh connect qemu:///session`

- SSH를 사용하여 원격 하이퍼바이저에 루트로 연결:

`virsh connect qemu+ssh://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명@호스트_명</span>`/system`
