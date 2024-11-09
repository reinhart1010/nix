---
layout: page
title: linux/farge (한국어)
description: "화면의 특정 픽셀 색상을 16진수 또는 RGB 형식으로 표시합니다."
content_hash: 2ec26f1cb5db136fa22f2f295771cac22c3a8b24
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/farge.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/farge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># farge

화면의 특정 픽셀 색상을 16진수 또는 RGB 형식으로 표시합니다.
더 많은 정보: <https://github.com/sdushantha/farge>.

- 픽셀의 색상을 작은 미리보기 창에 16진수 값으로 표시하고, 이 값을 클립보드에 복사:

`farge`

- 미리보기 창 없이 픽셀의 16진수 값을 클립보드에 복사:

`farge --no-preview`

- 픽셀의 16진수 값을 `stdout`에 출력하고, 이 값을 클립보드에 복사:

`farge --stdout`

- 픽셀의 RGB 값을 `stdout`에 출력하고, 이 값을 클립보드에 복사:

`farge --rgb --stdout`

- 픽셀의 16진수 값을 5000밀리초 동안 알림으로 표시하고, 이 값을 클립보드에 복사:

`farge --notify --expire-time 5000`
