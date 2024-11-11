---
layout: page
title: linux/gnome-screenshot (한국어)
description: "화면, 창 또는 사용자 정의 영역을 캡처하고 이미지를 파일로 저장합니다."
content_hash: d6693f3e96781ad9078f585adb05dd16447622b2
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/gnome-screenshot.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/gnome-screenshot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/gnome-screenshot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gnome-screenshot

화면, 창 또는 사용자 정의 영역을 캡처하고 이미지를 파일로 저장합니다.
더 많은 정보: <https://manned.org/gnome-screenshot>.

- 스크린샷을 찍고 기본 위치, 일반적으로 `~/Pictures`에 저장:

`gnome-screenshot`

- 스크린샷을 찍고 지정한 파일 위치에 저장:

`gnome-screenshot --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 스크린샷을 찍고 클립보드에 저장:

`gnome-screenshot --clipboard`

- 지정한 초 후에 스크린샷 찍기:

`gnome-screenshot --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- GNOME Screenshot GUI 실행:

`gnome-screenshot --interactive`

- 현재 창의 스크린샷을 찍고 지정한 파일 위치에 저장:

`gnome-screenshot --window --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정한 초 후에 스크린샷 찍고 클립보드에 저장:

`gnome-screenshot --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --clipboard`

- 버전 표시:

`gnome-screenshot --version`
