---
layout: page
title: linux/virt-viewer (한국어)
description: "가상 머신(VM)을 위한 최소한의 그래픽 인터페이스."
content_hash: 89741a07fea1740dddda3b227b1b81acfea5623e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/virt-viewer.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virt-viewer

가상 머신(VM)을 위한 최소한의 그래픽 인터페이스.
참고: '도메인'은 기존 VM의 이름, UUID 또는 ID를 의미합니다 (참조: tldr virsh).
더 많은 정보: <https://manned.org/virt-viewer>.

- 실행 중인 가상 머신을 선택할 수 있는 프롬프트로 `virt-viewer` 시작:

`virt-viewer`

- ID, UUID 또는 이름으로 특정 가상 머신에 대해 `virt-viewer` 시작:

`virt-viewer "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>`"`

- 가상 머신이 시작될 때까지 기다리고 종료 후 재시작되면 자동으로 다시 연결:

`virt-viewer --reconnect --wait "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>`"`

- TLS를 통해 특정 원격 가상 머신에 연결:

`virt-viewer --connect "xen//`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>`"`

- SSH를 통해 특정 원격 가상 머신에 연결:

`virt-viewer --connect "qemu+ssh//`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>`/system" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>`"`
