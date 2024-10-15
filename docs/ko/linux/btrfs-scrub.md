---
layout: page
title: linux/btrfs-scrub (한국어)
description: "btrfs 파일 시스템을 검사하여 데이터 무결성을 확인."
content_hash: 915bba76554b4f375603e26b3b5b709b2586c9d1
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-scrub.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs scrub

btrfs 파일 시스템을 검사하여 데이터 무결성을 확인.
한 달에 한 번 스크럽 실행을 권장.
더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- 스크럽 시작:

`sudo btrfs scrub start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_마운트</span>

- 진행 중이거나 마지막으로 완료된 스크럽 상태 보기:

`sudo btrfs scrub status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_마운트</span>

- 진행 중인 스크럽 취소:

`sudo btrfs scrub cancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_마운트</span>

- 이전에 취소된 스크럽 재개:

`sudo btrfs scrub resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_마운트</span>

- 스크럽을 시작하고 완료될 때까지 기다린 후 종료:

`sudo btrfs scrub start -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_마운트</span>

- 조용한 모드로 스크럽 시작 (오류나 통계를 출력하지 않음):

`sudo btrfs scrub start -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/btrfs_마운트</span>
