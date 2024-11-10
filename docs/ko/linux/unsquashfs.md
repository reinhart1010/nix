---
layout: page
title: linux/unsquashfs (한국어)
description: "squashfs 파일 시스템의 압축을 풀고, 파일을 추출하거나 나열합니다."
content_hash: f67e362f87f55736a44fdf1c6274183ef28810b0
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/unsquashfs.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/unsquashfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unsquashfs

squashfs 파일 시스템의 압축을 풀고, 파일을 추출하거나 나열합니다.
더 많은 정보: <https://manned.org/unsquashfs>.

- squashfs 파일 시스템을 현재 작업 디렉토리의 `squashfs-root`에 추출:

`unsquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_시스템.squashfs</span>

- squashfs 파일 시스템을 지정된 디렉토리에 추출:

`unsquashfs -dest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_시스템.squashfs</span>

- 파일이 추출될 때 파일 이름 표시:

`unsquashfs -info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_시스템.squashfs</span>

- 파일이 추출될 때 파일 이름과 속성 표시:

`unsquashfs -linfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_시스템.squashfs</span>

- squashfs 파일 시스템 내부의 파일 나열 (추출하지 않고):

`unsquashfs -ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_시스템.squashfs</span>

- squashfs 파일 시스템 내부의 파일과 속성 나열 (추출하지 않고):

`unsquashfs -lls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_시스템.squashfs</span>
