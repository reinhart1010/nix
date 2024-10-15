---
layout: page
title: linux/btrfs-filesystem (한국어)
description: "btrfs 파일 시스템 관리."
content_hash: 305a02e81aa8c3b8e9786081a609ba77cc9808bb
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/btrfs-filesystem.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-filesystem.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-filesystem.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-filesystem.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs filesystem

btrfs 파일 시스템 관리.
더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>.

- 파일 시스템 사용량 표시 (상세 정보를 보려면 root로 실행):

`btrfs filesystem usage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_마운트</span>

- 개별 장치별 사용량 표시:

`sudo btrfs filesystem show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_마운트</span>

- btrfs 파일 시스템에서 단일 파일 조각 모음 (중복 제거 에이전트 실행 중에는 피하십시오):

`sudo btrfs filesystem defragment -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 디렉토리를 재귀적으로 조각 모음 (서브볼륨 경계를 넘지 않음):

`sudo btrfs filesystem defragment -v -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 미기록된 데이터 블록을 디스크에 강제로 동기화:

`sudo btrfs filesystem sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_마운트</span>

- 디렉토리 내 파일의 디스크 사용량을 재귀적으로 요약:

`sudo btrfs filesystem du --summarize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
