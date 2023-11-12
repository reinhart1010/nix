---
layout: page
title: common/virsh-list (한국어)
description: "가상 머신의 ID, 이름, 상태 나열."
content_hash: 4267f8dd7e101b5f7177279aebfa2d89f6529af4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/virsh-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh-list

가상 머신의 ID, 이름, 상태 나열.
같이 보기: `virsh`.
더 많은 정보: <https://manned.org/virsh>.

- 실행 중인 가상 머신에 대한 정보 나열:

`virsh list`

- 상태에 관계없이 가상 머신에 대한 정보 나열:

`virsh list --all`

- 자동 시작이 활성화되거나 비활성화된 가상 머신에 대한 정보 나열:

`virsh list --all --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autostart|no-autostart</span>

- 스냅샷 유무에 관계없이 가상 머신에 대한 정보 나열:

`virsh list --all --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">with-snapshot|without-snapshot</span>
