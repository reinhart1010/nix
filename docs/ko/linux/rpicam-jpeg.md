---
layout: page
title: linux/rpicam-jpeg (한국어)
description: "Raspberry Pi 카메라를 사용하여 JPEG 이미지를 캡처하고 저장."
content_hash: 94133e036133d2d5ca94776ff8bd77252de5e0a6
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/rpicam-jpeg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rpicam-jpeg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpicam-jpeg

Raspberry Pi 카메라를 사용하여 JPEG 이미지를 캡처하고 저장.
더 많은 정보: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-jpeg>.

- 이미지를 캡처하고 파일명 지정:

`rpicam-jpeg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jpg</span>

- 설정된 크기로 이미지 캡처:

`rpicam-jpeg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jpg</span>` --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920</span>` --height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1080</span>

- 20초의 노출과 150%의 게인으로 이미지 캡처:

`rpicam-jpeg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jpg</span>` --shutter 20000 --gain 1.5`
