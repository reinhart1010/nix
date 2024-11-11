---
layout: page
title: linux/grim (한국어)
description: "Wayland 컴포지터에서 이미지를 캡처(스크린샷)합니다."
content_hash: 0ff01bffce50bbc92d8d22ba50b8be1d6fce51e1
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/grim.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/grim.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># grim

Wayland 컴포지터에서 이미지를 캡처(스크린샷)합니다.
더 많은 정보: <https://sr.ht/~emersion/grim>.

- 모든 출력의 스크린샷 캡처:

`grim`

- 특정 출력의 스크린샷 캡처:

`grim -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 특정 영역의 스크린샷 캡처:

`grim -g "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><x_위치>,<y_위치> <너비>x<높이></span>`"`

- 특정 영역을 선택하고 스크린샷 캡처 (slurp 사용):

`grim -g "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$(slurp)</span>`"`

- 사용자 정의 파일명 사용:

`grim "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>`"`

- 스크린샷을 캡처하고 클립보드에 복사:

`grim - | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클립보드_관리자</span>
