---
layout: page
title: linux/btrfs-restore (한국어)
description: "손상된 btrfs 파일 시스템에서 파일을 복구하려고 시도합니다."
content_hash: 89e0b18ff7521f6d25f502dabd58aa721a803f8a
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/btrfs-restore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-restore.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-restore.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/btrfs-restore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># btrfs restore

손상된 btrfs 파일 시스템에서 파일을 복구하려고 시도합니다.
더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- btrfs 파일 시스템에서 모든 파일을 지정된 디렉토리로 복원:

`sudo btrfs restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_폴더</span>

- btrfs 파일 시스템에서 복원할 파일 목록 표시 (복원하지 않음):

`sudo btrfs restore --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_폴더</span>

- 주어진 정규 표현식과 일치하는 파일을 btrfs 파일 시스템에서 복원 ([대]소문자 구분 없음, 대상 파일의 모든 상위 디렉토리도 일치해야 함):

`sudo btrfs restore --path-regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규식</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_폴더</span>

- 특정 루트 트리 `bytenr`를 사용하여 btrfs 파일 시스템에서 파일 복원 (`btrfs-find-root` 참조):

`sudo btrfs restore -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bytenr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_폴더</span>

- btrfs 파일 시스템에서 메타데이터, 확장 속성, 심볼릭 링크와 함께 파일을 복원하여 대상의 파일을 덮어쓰기:

`sudo btrfs restore --metadata --xattr --symlinks --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_폴더</span>
