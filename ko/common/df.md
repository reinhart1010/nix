---
layout: page
title: common/df (한국어)
description: "파일 시스템 디스크 공간 사용량에 대한 개요를 제공합니다."
content_hash: 3d1694733f6a08ed47da2df536f7db8bd57a7896
related_topics:
  - title: Deutsch version
    url: /de/common/df.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/df.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/df.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/df.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/df.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># df

파일 시스템 디스크 공간 사용량에 대한 개요를 제공합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/df>.

- 모든 파일 시스템들과 그들의 디스크 사용량 출력:

`df`

- 사람이 읽을 수 있는 형태로 모든 파일시스템들과 그들의 디스크 사용량 출력:

`df -h`

- 주어진 파일이나 디렉토리를 포함하는 파일 시스템과 그것의 디스크 사용량 출력:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일_혹은_디렉토리명</span>

- 사용 가능한 inode들의 수에 대한 통계 출력:

`df -i`
