---
layout: page
title: linux/eselect-kernel (한국어)
description: "`/usr/src/linux` 심볼릭 링크를 관리하기 위한 `eselect` 모듈."
content_hash: 15b2c0cc89c3da4f5d0c9bd3518a259e72002435
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/eselect-kernel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eselect kernel

`/usr/src/linux` 심볼릭 링크를 관리하기 위한 `eselect` 모듈.
더 많은 정보: <https://wiki.gentoo.org/wiki/Eselect#Kernel>.

- 사용 가능한 커널 심볼릭 링크 대상과 해당 번호 나열:

`eselect kernel list`

- `list` 명령어의 이름이나 번호로 `/usr/src/linux` 심볼릭 링크 설정:

`eselect kernel set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|번호</span>

- 현재 커널 심볼릭 링크가 가리키는 대상을 표시:

`eselect kernel show`

- 현재 실행 중인 커널로 커널 심볼릭 링크 설정:

`eselect kernel update`
