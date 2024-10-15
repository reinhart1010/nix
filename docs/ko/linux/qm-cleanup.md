---
layout: page
title: linux/qm-cleanup (한국어)
description: "QEMU/KVM 가상 머신 관리자에서 tap 장치, VGPU 등과 같은 리소스를 정리."
content_hash: b3466f9e1be38ecefb6299de30fac2065848e5e4
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/qm-cleanup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm cleanup

QEMU/KVM 가상 머신 관리자에서 tap 장치, VGPU 등과 같은 리소스를 정리.
VM 종료, 충돌 후 호출됩니다.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 리소스 정리:

`qm cleanup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clean-shutdown</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest-requested</span>
