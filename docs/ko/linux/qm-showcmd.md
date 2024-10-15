---
layout: page
title: linux/qm-showcmd (한국어)
description: "VM을 시작하는 데 사용된 명령줄을 표시 (디버그 정보)."
content_hash: 86ee454cc65b89b5ae89965073d7d8f44c9c364e
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/qm-showcmd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm showcmd

VM을 시작하는 데 사용된 명령줄을 표시 (디버그 정보).
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 특정 가상 머신의 명령줄 표시:

`qm showcmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 각 옵션을 새 줄에 배치하여 가독성 향상:

`qm showcmd --pretty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 특정 스냅샷에서 구성 값 가져오기:

`qm showcmd --snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>
