---
layout: page
title: linux/btrfs-balance (한국어)
description: "btrfs 파일 시스템에서 블록 그룹을 균형 조정."
content_hash: 17518cb15ebf91bf88b290ffc3e83827c552dad4
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/btrfs-balance.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-balance.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/btrfs-balance.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># btrfs balance

btrfs 파일 시스템에서 블록 그룹을 균형 조정.
더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-balance.html>.

- 실행 중이거나 일시 중지된 균형 조정 작업 상태 표시:

`sudo btrfs balance status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_파일시스템</span>

- 모든 블록 그룹 균형 조정 (느림; 파일 시스템의 모든 블록을 다시 씀):

`sudo btrfs balance start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_파일시스템</span>

- 사용률이 15% 미만인 데이터 블록 그룹을 백그라운드에서 균형 조정:

`sudo btrfs balance start --bg -dusage=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_파일시스템</span>

- 주어진 장치 `devid`에 사용률 20% 미만이고 최소 1개의 청크가 있는 최대 10개의 메타데이터 청크 균형 조정 (btrfs filesystem show 참고):

`sudo btrfs balance start -musage=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>`,limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`,devid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">devid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_파일시스템</span>

- 데이터 블록을 raid6로, 메타데이터를 raid1c3로 변환 (프로필은 mkfs.btrfs(8) 참고):

`sudo btrfs balance start -dconvert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raid6</span>` -mconvert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raid1c3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_파일시스템</span>

- 이미 변환된 청크를 건너뛰고 데이터 블록을 raid1로 변환 (예: 이전에 취소된 변환 작업 후):

`sudo btrfs balance start -dconvert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raid1</span>`,soft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_파일시스템</span>

- 실행 중이거나 일시 중지된 균형 조정 작업 취소, 일시 중지 또는 재개:

`sudo btrfs balance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cancel|pause|resume</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_파일시스템</span>
