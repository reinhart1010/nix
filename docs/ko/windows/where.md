---
layout: page
title: windows/where (한국어)
description: "검색 패턴과 일치하는 파일의 위치를 표시합니다."
content_hash: d93316ca7743f61f89f2acdc2915cee3bbc541ae
last_modified_at: 2024-10-09
related_topics:
  - title: বাংলা version
    url: /bn/windows/where.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/where.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/windows/where.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/where.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/where.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/where.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># where

검색 패턴과 일치하는 파일의 위치를 표시합니다.
기본적으로 현재 작업 디렉토리와 PATH 환경 변수의 경로를 폴더로 설정합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/where>.

- 파일 패턴의 위치 표시:

`where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_패턴</span>

- 파일 크기와 날짜를 포함하여 파일 패턴의 위치 표시:

`where /T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_패턴</span>

- 지정된 경로에서 파일 패턴을 재귀적으로 검색:

`where /R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_패턴</span>

- 파일 패턴의 위치에 대한 오류 코드를 자동으로 반환:

`where /Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_패턴</span>
