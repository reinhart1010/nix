---
layout: page
title: linux/btrfs-inspect-internal (한국어)
description: "btrfs 파일 시스템의 내부 정보를 쿼리."
content_hash: 3e7b67a3d54d4ea706b0e8ac24c9f3ff24d84530
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/btrfs-inspect-internal.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-inspect-internal.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-inspect-internal.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/btrfs-inspect-internal.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># btrfs inspect-internal

btrfs 파일 시스템의 내부 정보를 쿼리.
더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-inspect-internal.html>.

- 슈퍼블록 정보 출력:

`sudo btrfs inspect-internal dump-super `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>

- 슈퍼블록 및 모든 복사본의 정보 출력:

`sudo btrfs inspect-internal dump-super --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>

- 파일 시스템 메타데이터 정보 출력:

`sudo btrfs inspect-internal dump-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>

- `n`번째 inode의 파일 목록 출력:

`sudo btrfs inspect-internal inode-resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_마운트</span>

- 지정된 논리 주소에 있는 파일 목록 출력:

`sudo btrfs inspect-internal logical-resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">논리_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_마운트</span>

- 루트, extent, csum 및 fs 트리의 통계 출력:

`sudo btrfs inspect-internal tree-stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>
