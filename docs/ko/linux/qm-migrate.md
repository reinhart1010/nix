---
layout: page
title: linux/qm-migrate (한국어)
description: "가상 머신을 마이그레이션."
content_hash: 27f0e4393c0d1be36001fac765a79330b056c1a4
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/qm-migrate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm migrate

가상 머신을 마이그레이션.
새로운 마이그레이션 작업을 생성하는 데 사용됩니다.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 특정 가상 머신 마이그레이션:

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- 현재 I/O 대역폭 제한을 10 KiB/s로 재정의:

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` --bwlimit 10`

- 로컬 장치를 사용하는 가상 머신의 마이그레이션 허용 (루트 전용):

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` --force true`

- 가상 머신이 실행 중인 경우 온라인/라이브 마이그레이션 사용:

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` --online true`

- 로컬 디스크에 대한 라이브 스토리지 마이그레이션 활성화:

`qm migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` --with-local-disks true`
