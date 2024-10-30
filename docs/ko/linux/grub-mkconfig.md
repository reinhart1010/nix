---
layout: page
title: linux/grub-mkconfig (한국어)
description: "GRUB 구성 파일 생성."
content_hash: 616d3a7235e138ddeb6b4d2ca292df6134e7e578
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/linux/grub-mkconfig.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/grub-mkconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/grub-mkconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grub-mkconfig

GRUB 구성 파일 생성.
더 많은 정보: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dmkconfig.html>.

- 시뮬레이션을 실행하고 구성을 `stdout`에 출력:

`sudo grub-mkconfig`

- 구성 파일 생성:

`sudo grub-mkconfig --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/boot/grub/grub.cfg</span>

- 도움말 표시:

`grub-mkconfig --help`
