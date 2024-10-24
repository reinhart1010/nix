---
layout: page
title: linux/qm-disk-move (한국어)
description: "Proxmox 클러스터 내에서 가상 디스크를 한 스토리지에서 다른 스토리지로 이동."
content_hash: 84142c4145be7f865fca2fb208da831b19394c16
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/qm-disk-move.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/qm-disk-move.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm disk move

Proxmox 클러스터 내에서 가상 디스크를 한 스토리지에서 다른 스토리지로 이동.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 가상 디스크 이동:

`qm disk move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색인</span>

- 이전 가상 디스크 복사본 삭제:

`qm disk move -delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색인</span>
