---
layout: page
title: linux/qm-reset (한국어)
description: "QEMU/KVM 가상 머신 관리자에서 가상 머신을 재설정합니다."
content_hash: a11a7a15ca6241af090add3196469ac76fe51428
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/qm-reset.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm reset

QEMU/KVM 가상 머신 관리자에서 가상 머신을 재설정합니다.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 가상 머신 재설정:

`qm reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 가상 머신을 재설정하고 잠금 건너뛰기 (루트만 이 옵션을 사용할 수 있음):

`qm reset --skiplock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>
