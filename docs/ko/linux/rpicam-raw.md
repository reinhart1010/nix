---
layout: page
title: linux/rpicam-raw (한국어)
description: "Raspberry Pi 카메라에서 raw 비디오를 캡처합니다."
content_hash: 6a1022b321252862c13ec801e3db81c6a109fb3c
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/rpicam-raw.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rpicam-raw

Raspberry Pi 카메라에서 raw 비디오를 캡처합니다.
더 많은 정보: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-raw>.

- 특정 초 동안 비디오 캡처:

`rpicam-raw -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2000</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.raw</span>

- 비디오 크기 및 프레임 속도 변경:

`rpicam-raw -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>` --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4056</span>` --height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3040</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.raw</span>` --framerate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>
