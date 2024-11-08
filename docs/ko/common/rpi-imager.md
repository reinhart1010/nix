---
layout: page
title: common/rpi-imager (한국어)
description: "이미지를 저장 장치에 플래시."
content_hash: fa00cc74e6b57b95c899a39ad8486acb648c16e2
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rpi-imager.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rpi-imager

이미지를 저장 장치에 플래시.
더 많은 정보: <https://github.com/raspberrypi/rpi-imager>.

- 특정 이미지를 특정 블록 장치에 기록:

`rpi-imager --cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 체크섬 검증을 비활성화한 상태로 특정 이미지를 블록 장치에 기록:

`rpi-imager --cli --disable-verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 검증 시 특정 체크섬을 기대하는 상태로 특정 이미지를 블록 장치에 기록:

`rpi-imager --cli --sha256 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기대_해시</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
