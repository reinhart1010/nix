---
layout: page
title: linux/qm-snapshot (한국어)
description: "가상 머신 스냅샷 생성."
content_hash: 107d7b43fb7804e6a73e34a01b754753d9d4e920
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/qm-snapshot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm snapshot

가상 머신 스냅샷 생성.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 특정 가상 머신의 스냅샷 생성:

`qm snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_이름</span>

- 특정 설명과 함께 스냅샷 생성:

`qm snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_이름</span>` --description `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설명</span>

- vmstate를 포함한 스냅샷 생성:

`qm snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_이름</span>` --description `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설명</span>` --vmstate 1`
