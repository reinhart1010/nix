---
layout: page
title: linux/btrfs-check (한국어)
description: "btrfs 파일 시스템 검사 또는 복구."
content_hash: acf54c67e291d809b1fc9704f1e18b9000768cad
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/btrfs-check.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-check.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-check.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/btrfs-check.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># btrfs check

btrfs 파일 시스템 검사 또는 복구.
더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-check.html>.

- btrfs 파일 시스템 검사:

`sudo btrfs check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>

- btrfs 파일 시스템 검사 및 복구 (위험함):

`sudo btrfs check --repair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>

- 검사 진행 상황 표시:

`sudo btrfs check --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>

- 각 데이터 블록의 체크섬 확인 (파일 시스템이 손상되지 않은 경우):

`sudo btrfs check --check-data-csum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>

- `n`번째 슈퍼블록 사용 (`n`은 0, 1 또는 2 가능):

`sudo btrfs check --super `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>

- 체크섬 트리 재구성:

`sudo btrfs check --repair --init-csum-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>

- 익스텐트 트리 재구성:

`sudo btrfs check --repair --init-extent-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>
