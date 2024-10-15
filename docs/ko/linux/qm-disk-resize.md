---
layout: page
title: linux/qm-disk-resize (한국어)
description: "Proxmox Virtual Environment (PVE)에서 가상 머신 디스크 크기 조정."
content_hash: 57c8fbb2510048bf066bcaa34ff1ea3a75555c78
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/qm-disk-resize.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/qm-disk-resize.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm disk resize

Proxmox Virtual Environment (PVE)에서 가상 머신 디스크 크기 조정.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 가상 디스크에 `n` 기가바이트 추가:

`qm disk resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스크_이름</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>`G`
