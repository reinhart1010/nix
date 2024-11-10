---
layout: page
title: linux/parted (한국어)
description: "파티션 조작 프로그램."
content_hash: 8816b8861102f13fed2f11aef2e7bf7940e6f6b5
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/parted.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/parted.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/parted.html
    icon: bi bi-globe
tldri18n_status: 2
---
# parted

파티션 조작 프로그램.
같이 보기: `partprobe`.
더 많은 정보: <https://www.gnu.org/software/parted/parted.html>.

- 모든 블록 디바이스의 파티션 나열:

`sudo parted --list`

- 지정된 디스크를 선택하여 대화형 모드 시작:

`sudo parted `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 지정된 레이블 유형의 새 파티션 테이블 생성:

`sudo parted --script `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>` mklabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun</span>

- 대화형 모드에서 파티션 정보 표시:

`print`

- 대화형 모드에서 디스크 선택:

`select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 대화형 모드에서 지정된 파일 시스템으로 16GB 파티션 생성:

`mkpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primary|logical|extended</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16G</span>

- 대화형 모드에서 파티션 크기 조정:

`resizepart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_끝_위치</span>

- 대화형 모드에서 파티션 제거:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
