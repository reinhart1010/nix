---
layout: page
title: linux/btrfs-property (한국어)
description: "BTRFS 파일 시스템 객체(파일, 디렉터리, 서브볼륨, 파일 시스템 또는 장치)에 대한 속성을 가져오거나 설정하거나 나열합니다."
content_hash: ac015f8a08088b4486d2bf1b8720f59053439f58
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/btrfs-property.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-property.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/btrfs-property.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># btrfs property

BTRFS 파일 시스템 객체(파일, 디렉터리, 서브볼륨, 파일 시스템 또는 장치)에 대한 속성을 가져오거나 설정하거나 나열합니다.
더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-property.html>.

- 주어진 btrfs 객체에 대해 사용 가능한 속성(및 설명)을 나열:

`sudo btrfs property list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_객체</span>

- 주어진 btrfs 객체의 모든 속성을 가져오기:

`sudo btrfs property get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_객체</span>

- 주어진 btrfs 파일 시스템 또는 장치의 `label` 속성을 가져오기:

`sudo btrfs property get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_파일시스템</span>` label`

- 주어진 btrfs 파일 시스템 또는 장치의 모든 객체 유형별 속성을 가져오기:

`sudo btrfs property get -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subvol|filesystem|inode|device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_파일시스템</span>

- 주어진 btrfs inode(파일 또는 디렉터리)의 `compression` 속성을 설정:

`sudo btrfs property set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_inode</span>` compression `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zstd|zlib|lzo|none</span>
