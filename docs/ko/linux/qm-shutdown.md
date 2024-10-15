---
layout: page
title: linux/qm-shutdown (한국어)
description: "QEMU/KVM 가상 머신 관리자에서 가상 머신 종료."
content_hash: 14ebc249cfc6a9bd340c8df603c25c24ad352fa4
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/qm-shutdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm shutdown

QEMU/KVM 가상 머신 관리자에서 가상 머신 종료.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 가상 머신 종료:

`qm shutdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 최대 10초 대기 후 가상 머신 종료:

`qm shutdown --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 저장소 볼륨을 비활성화하지 않고 가상 머신 종료:

`qm shutdown --keepActive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 잠금을 건너뛰고 가상 머신 종료 (루트 사용자만 사용 가능):

`qm shutdown --skiplock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 가상 머신을 정지하고 종료:

`qm shutdown --forceStop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>
