---
layout: page
title: linux/mkfs.erofs (한국어)
description: "이미지 내에 EROFS 파일 시스템 생성."
content_hash: 9c6828db3c8bf80ad1a39944465799ec7f5c2aca
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/mkfs.erofs.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/mkfs.erofs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.erofs

이미지 내에 EROFS 파일 시스템 생성.
더 많은 정보: <https://erofs.docs.kernel.org/en/latest/>.

- 루트 디렉토리를 기반으로 EROFS 파일 시스템 생성:

`mkfs.erofs image.erofs root/`

- 특정 UUID를 가진 EROFS 이미지 생성:

`mkfs.erofs -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UUID</span>` image.erofs root/`

- 압축된 EROFS 이미지 생성:

`mkfs.erofs -zlz4hc image.erofs root/`

- 모든 파일의 소유자가 root인 EROFS 이미지 생성:

`mkfs.erofs --all-root image.erofs root/`
