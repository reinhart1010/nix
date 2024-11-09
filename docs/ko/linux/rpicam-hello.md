---
layout: page
title: linux/rpicam-hello (한국어)
description: "Raspberry Pi 카메라를 사용하여 실시간 카메라 스트림 보기."
content_hash: 41dfd6af54c7b7a1adc071c520edc9965df6f63a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/rpicam-hello.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rpicam-hello.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpicam-hello

Raspberry Pi 카메라를 사용하여 실시간 카메라 스트림 보기.
더 많은 정보: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-hello>.

- 특정 시간(밀리초) 동안 카메라 미리보기 스트림 표시:

`rpicam-hello -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간</span>

- 특정 카메라 센서를 위한 설정 조정:

`rpicam-hello --tuning-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/share/libcamera/ipa/rpi/경로/대상/config.json</span>
