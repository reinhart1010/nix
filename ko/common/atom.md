---
layout: page
title: common/atom (한국어)
description: "플러그 기능이 있는 교차 플랫폼 텍스트 편집기."
content_hash: 2f5dc19cf3129ab879f655dac19fea3f73c36e3b
related_topics:
  - title: Deutsch version
    url: /de/common/atom.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/atom.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atom.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atom.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/atom.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atom.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/atom.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/atom.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># atom

플러그 기능이 있는 교차 플랫폼 텍스트 편집기.
플러그는 `apm`에 의해 관리됩니다.
더 많은 정보: <https://atom.io/>.

- 파일이나 디렉토리 열기:

`atom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명_또는_디렉토리명</span>

- 새로운 창에서 파일이나 디렉토리 열기:

`atom -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명_또는_디렉토리명</span>

- 현재 창에서 파일이나 디렉토리 열기:

`atom --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명_또는_디렉토리명</span>

- 안전모드에서 atom 열기Open atom in safe mode (추가 패키지를 로드하지 마시오):

`atom --safe`

- 백그라운드에서 fork하지 않도록 막기, atom을 터미널에 부착합니다:

`atom --foreground`
