---
layout: page
title: linux/btrfs-device (한국어)
description: "btrfs 파일 시스템에서 장치 관리."
content_hash: ac0210a3adb8562a225d903bdd2ebe7d7408715f
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/btrfs-device.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-device.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-device.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-device.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/btrfs-device.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># btrfs device

btrfs 파일 시스템에서 장치 관리.
더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- btrfs 파일 시스템에 하나 이상의 장치 추가:

`sudo btrfs device add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/블록_장치1</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/블록_장치2</span>`] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_파일_시스템</span>

- btrfs 파일 시스템에서 장치 제거:

`sudo btrfs device remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치|장치_ID</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>`]`

- 오류 통계 표시:

`sudo btrfs device stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_파일_시스템</span>

- 모든 디스크를 스캔하고 감지된 모든 btrfs 파일 시스템을 커널에 알림:

`sudo btrfs device scan --all-devices`

- 디스크별 할당 통계 자세히 표시:

`sudo btrfs device usage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_파일_시스템</span>
