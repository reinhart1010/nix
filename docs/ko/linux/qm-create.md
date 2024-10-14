---
layout: page
title: linux/qm-create (한국어)
description: "QEMU/KVM 가상 머신 관리자에서 가상 머신을 생성하거나 복원."
content_hash: 7d34ca7a6ca6fa622bffdb3d669ff8cc7c594dd0
last_modified_at: 2024-10-14
related_topics:
  - title: Deutsch version
    url: /de/linux/qm-create.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/qm-create.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-create.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm create

QEMU/KVM 가상 머신 관리자에서 가상 머신을 생성하거나 복원.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 가상 머신 생성:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- 생성 후 자동으로 머신 시작:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --start 1`

- 머신의 운영 체제 유형 지정:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --ostype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">win10</span>

- 기존 머신 교체(아카이브 필요):

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/백업_파일.tar</span>` --force 1`

- 가상 머신의 상태에 따라 자동으로 실행되는 스크립트 지정:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --hookscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.pl</span>
