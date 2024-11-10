---
layout: page
title: linux/rpicam-hello (한국어)
description: "Raspberry Pi 카메라를 사용하여 실시간 카메라 스트림 보기."
content_hash: 41dfd6af54c7b7a1adc071c520edc9965df6f63a
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/rpicam-hello.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rpicam-hello

Raspberry Pi 카메라를 사용하여 실시간 카메라 스트림 보기.
더 많은 정보: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-hello>.

- 특정 시간(밀리초) 동안 카메라 미리보기 스트림 표시:

`rpicam-hello -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간</span>

- 특정 카메라 센서를 위한 설정 조정:

`rpicam-hello --tuning-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/share/libcamera/ipa/rpi/경로/대상/config.json</span>
