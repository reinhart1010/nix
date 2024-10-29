---
layout: page
title: linux/xrdb (한국어)
description: "유닉스 계열 시스템을 위한 X 윈도우 서버의 리소스 데이터베이스 도구."
content_hash: 6955533ab3cdc1619d0e54413ee0957900402e07
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/xrdb.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/xrdb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xrdb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xrdb

유닉스 계열 시스템을 위한 X 윈도우 서버의 리소스 데이터베이스 도구.
더 많은 정보: <https://www.x.org/releases/X11R7.7/doc/man/man1/xrdb.1.xhtml>.

- 대화형 모드로 `xrdb` 시작:

`xrdb`

- 리소스 파일에서 값(예: 스타일 규칙) 불러오기:

`xrdb -load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.Xresources</span>

- 리소스 데이터베이스를 조회하고 현재 설정된 값 출력:

`xrdb -query`
