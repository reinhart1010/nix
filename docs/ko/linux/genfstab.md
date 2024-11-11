---
layout: page
title: linux/genfstab (한국어)
description: "Arch Linux 설치 스크립트로, fstab 파일에 추가할 수 있는 출력 생성."
content_hash: a5bc9556cd3de2dda8df51ee9212ac9fefec185e
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/genfstab.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/genfstab.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># genfstab

Arch Linux 설치 스크립트로, fstab 파일에 추가할 수 있는 출력 생성.
더 많은 정보: <https://manned.org/genfstab.8>.

- 볼륨 레이블을 기반으로 fstab 호환 출력을 표시:

`genfstab -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>

- 볼륨 UUID를 기반으로 fstab 호환 출력을 표시:

`genfstab -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>

- 일반적으로 fstab 파일을 생성하는 방법, 루트 권한 필요:

`genfstab -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt/etc/fstab</span>

- 볼륨을 fstab 파일에 추가하여 자동으로 마운트:

`genfstab -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>` | sudo tee -a /etc/fstab`
