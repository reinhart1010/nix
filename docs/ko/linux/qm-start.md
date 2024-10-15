---
layout: page
title: linux/qm-start (한국어)
description: "QEMU/KVM 가상 머신 관리자에서 가상 머신 시작."
content_hash: f27d073418160954b8e8f1c4168d3e15b991cd7f
last_modified_at: 2024-10-15
related_topics:
  - title: Deutsch version
    url: /de/linux/qm-start.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/qm-start.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm start

QEMU/KVM 가상 머신 관리자에서 가상 머신 시작.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 특정 가상 머신 시작:

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- QEMU 머신 유형(즉, 에뮬레이트할 CPU) 지정:

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">q35</span>

- 60초의 타임아웃을 설정하여 특정 가상 머신 시작:

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>
