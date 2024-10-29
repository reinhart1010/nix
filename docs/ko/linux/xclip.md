---
layout: page
title: linux/xclip (한국어)
description: "X11 클립보드 조작 도구로, `xsel`과 유사합니다."
content_hash: d9a40e230f9e7eec3f7fade370dd62c2cc29d06d
last_modified_at: 2024-10-29
related_topics:
  - title: العربية version
    url: /ar/linux/xclip.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/xclip.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/xclip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/xclip.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xclip.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xclip

X11 클립보드 조작 도구로, `xsel`과 유사합니다.
X 기본 및 보조 선택 영역과 시스템 클립보드(`Ctrl + C`/`Ctrl + V`)를 처리합니다.
같이 보기: `wl-copy`.
더 많은 정보: <https://manned.org/xclip>.

- 명령의 출력을 X11 기본 선택 영역(클립보드)에 복사:

`echo 123 | xclip`

- 명령의 출력을 지정된 X11 선택 영역에 복사:

`echo 123 | xclip -selection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primary|secondary|clipboard</span>

- 명령의 출력을 시스템 클립보드에 짧은 표기법을 사용하여 복사:

`echo 123 | xclip -sel clip`

- 파일의 내용을 시스템 클립보드에 복사:

`xclip -sel clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일.txt</span>

- PNG 파일의 내용을 시스템 클립보드에 복사 (다른 프로그램에 올바르게 붙여넣기 가능):

`xclip -sel clip -t image/png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일.png</span>

- 콘솔에서 사용자 입력을 시스템 클립보드에 복사:

`xclip -i`

- X11 기본 선택 영역의 내용을 콘솔에 붙여넣기:

`xclip -o`

- 시스템 클립보드의 내용을 콘솔에 붙여넣기:

`xclip -o -sel clip`
