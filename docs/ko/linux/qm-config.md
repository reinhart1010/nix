---
layout: page
title: linux/qm-config (한국어)
description: "적용 대기 중인 구성 변경 사항을 포함하여 가상 머신 구성을 표시."
content_hash: 32442f4391daef7732f1c2697230e36d4b04a7af
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/qm-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm config

적용 대기 중인 구성 변경 사항을 포함하여 가상 머신 구성을 표시.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 가상 머신 구성 표시:

`qm config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 가상 머신에 대한 현재 구성 값을 표시 (대기 중인 값 대신):

`qm config --current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- 지정된 스냅샷에서 구성 값 가져오기:

`qm config --snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>
