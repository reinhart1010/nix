---
layout: page
title: linux/dracut (한국어)
description: "Linux 커널을 부팅하기 위한 initramfs 이미지를 생성합니다."
content_hash: 75accf88ad2622bef4c7f6661877a2201dab8fb1
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/dracut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dracut

Linux 커널을 부팅하기 위한 initramfs 이미지를 생성합니다.
Dracut은 기본적으로 `/etc/dracut.conf`, `/etc/dracut.conf.d/*.conf`, `/usr/lib/dracut/dracut.conf.d/*.conf`의 구성 파일에서 옵션을 사용합니다.
더 많은 정보: <https://github.com/dracutdevs/dracut/wiki>.

- 현재 커널에 대한 initramfs 이미지를 옵션을 덮어쓰지 않고 생성:

`dracut`

- 현재 커널에 대한 initramfs 이미지를 생성하고 기존 이미지를 덮어씀:

`dracut --force`

- 특정 커널에 대한 initramfs 이미지 생성:

`dracut --kver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커널_버전</span>

- 사용 가능한 모듈 나열:

`dracut --list-modules`
