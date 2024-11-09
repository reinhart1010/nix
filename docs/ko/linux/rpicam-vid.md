---
layout: page
title: linux/rpicam-vid (한국어)
description: "Raspberry Pi 카메라를 사용하여 비디오를 촬영합니다."
content_hash: 87698e8908901ab9960e63fececd3baaaf423cca
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/rpicam-vid.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rpicam-vid.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpicam-vid

Raspberry Pi 카메라를 사용하여 비디오를 촬영합니다.
같이 보기: `vlc`.
더 많은 정보: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-vid>.

- 10초 비디오 촬영:

`rpicam-vid -t 10000 -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.h264</span>
