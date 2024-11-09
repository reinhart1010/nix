---
layout: page
title: common/shotcut (한국어)
description: "비디오 편집 프로그램."
content_hash: 2e207292229d8cd6664bf9c51c5b0970db829d72
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/shotcut.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/shotcut.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/shotcut.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># shotcut

비디오 편집 프로그램.
더 많은 정보: <https://shotcut.org/notes/command-line-options/>.

- Shotcut 시작:

`shotcut`

- 오디오/비디오 파일 열기:

`shotcut `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 오디오 드라이버로 시작:

`shotcut --SDL_AUDIODRIVER "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pulseaudio</span>`"`

- 전체 화면으로 시작:

`shotcut --fullscreen`

- GPU 처리로 시작:

`shotcut --gpu`
