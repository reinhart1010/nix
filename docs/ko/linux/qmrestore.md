---
layout: page
title: linux/qmrestore (한국어)
description: "QemuServer의 `vzdump` 백업 복원."
content_hash: 141444bd66e8da1daf1555808186405c968da32d
last_modified_at: 2024-10-14
related_topics:
  - title: Deutsch version
    url: /de/linux/qmrestore.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/qmrestore.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qmrestore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qmrestore

QemuServer의 `vzdump` 백업 복원.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qmrestore.1.html>.

- 원본 스토리지에 있는 백업 파일에서 가상 머신 복원:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- 원본 스토리지에 있는 백업 파일에서 기존 가상 머신 덮어쓰기:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --force true`

- 특정 스토리지에 있는 백업 파일에서 가상 머신 복원:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --storage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local</span>

- 백업에서 즉시 가상 머신 시작하고 백그라운드에서 복원 진행 (Proxmox Backup Server에서만 가능):

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --live-restore true`
