---
layout: page
title: linux/btrfs-subvolume (한국어)
description: "btrfs 서브볼륨과 스냅샷 관리."
content_hash: 5cb9e866747de3bae2a5adc1335518b297a91a95
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/btrfs-subvolume.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-subvolume.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-subvolume.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-subvolume.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs subvolume

btrfs 서브볼륨과 스냅샷 관리.
더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>.

- 새 빈 서브볼륨 생성:

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운_서브볼륨</span>

- 지정된 파일 시스템의 모든 서브볼륨과 스냅샷 나열:

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_파일시스템</span>

- 서브볼륨 삭제:

`sudo btrfs subvolume delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서브볼륨</span>

- 기존 서브볼륨의 읽기 전용 스냅샷 생성:

`sudo btrfs subvolume snapshot -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_서브볼륨</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상</span>

- 기존 서브볼륨의 읽기-쓰기 스냅샷 생성:

`sudo btrfs subvolume snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_서브볼륨</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상</span>

- 서브볼륨에 대한 자세한 정보 표시:

`sudo btrfs subvolume show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서브볼륨</span>
