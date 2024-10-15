---
layout: page
title: linux/qm-disk-import (한국어)
description: "디스크 이미지를 가상 머신에 비사용 디스크로 가져오기."
content_hash: f71c36407937fdc6573bcc32398ec807b0e583b7
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/qm-disk-import.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/qm-disk-import.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm disk import

디스크 이미지를 가상 머신에 비사용 디스크로 가져오기.
`qemu-img`에서 지원하는 이미지 형식(raw, qcow2, qed, vdi, vmdk, vhd)을 사용해야 함.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 특정 스토리지 이름을 사용하여 VMDK/qcow2/raw 디스크 이미지 가져오기:

`qm importdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디스크</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qcow2|raw|vmdk</span>
