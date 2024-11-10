---
layout: page
title: linux/rpicam-still (한국어)
description: "Raspberry Pi 카메라를 사용하여 사진을 촬영하고 저장하며, `rpicam-jpeg`에서 누락된 레거시 기능을 포함합니다."
content_hash: a2433e92cedf279324a0a454e0133f059dd5cb1e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/rpicam-still.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rpicam-still

Raspberry Pi 카메라를 사용하여 사진을 촬영하고 저장하며, `rpicam-jpeg`에서 누락된 레거시 기능을 포함합니다.
더 많은 정보: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-still>.

- 다른 인코딩 방식으로 사진 촬영:

`rpicam-still -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bmp|png|rgb|yuv420</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bmp|png|rgb|yuv420}</span>`}`

- RAW 이미지 촬영:

`rpicam-still -r -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jpg</span>

- 100초 노출 이미지 촬영:

`rpicam-still -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jpg</span>` --shutter 100000`
