---
layout: page
title: common/df (한국어)
description: "파일 시스템 디스크 공간 사용량에 대한 개요를 제공합니다."
content_hash: 3d1694733f6a08ed47da2df536f7db8bd57a7896
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/df.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/df.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/df.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/df.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/df.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/df.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/df.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/df.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/df.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

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
