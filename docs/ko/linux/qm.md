---
layout: page
title: linux/qm (한국어)
description: "QEMU/KVM 가상 머신 관리자."
content_hash: 5ddf4f79a6ee0ac0f80a9020bac96a4cca6875c0
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/qm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm

QEMU/KVM 가상 머신 관리자.
`list`, `start`, `stop`, `clone` 등의 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 모든 가상 머신 나열:

`qm list`

- 로컬 스토리지에 업로드된 ISO 파일을 사용하여 `local-lvm` 스토리지에 4 GB IDE 디스크와 ID가 100인 가상 머신 생성:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` -ide0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local-lvm:4</span>` -net0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">e1000</span>` -cdrom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local:iso/proxmox-mailgateway_2.1.iso</span>

- 가상 머신의 ID를 지정하여 구성 보기:

`qm config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- 특정 가상 머신 시작:

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- 종료 요청을 보내고, 가상 머신이 중지될 때까지 대기:

`qm shutdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` && qm wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- 가상 머신을 제거하고 모든 관련 리소스 삭제:

`qm destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --purge`
