---
layout: page
title: linux/qm-stop (한국어)
description: "가상 머신 중지."
content_hash: 5d191de053c8595d3e5c3792ae49a6f1679e9b55
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/qm-stop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm stop

가상 머신 중지.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 가상 머신을 즉시 중지:

`qm stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 가상 머신을 중지하고 최대 10초 기다리기:

`qm stop --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 가상 머신을 중지하고 잠금을 건너뜀 (루트 사용자만 이 옵션 사용 가능):

`qm stop --skiplock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 가상 머신을 중지하고 스토리지 볼륨 비활성화하지 않음:

`qm stop --keepActive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>
