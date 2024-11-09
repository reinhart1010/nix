---
layout: page
title: linux/dex (한국어)
description: "DesktopEntry Execution은 응용 프로그램 유형의 DesktopEntry 파일을 생성하고 실행하는 프로그램입니다."
content_hash: 615912ded0abe06e8a83efef13c1a54b94a44b36
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/dex.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/dex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dex

DesktopEntry Execution은 응용 프로그램 유형의 DesktopEntry 파일을 생성하고 실행하는 프로그램입니다.
더 많은 정보: <https://github.com/jceb/dex>.

- 자동 시작 폴더의 모든 프로그램 실행:

`dex --autostart`

- 지정된 폴더의 모든 프로그램 실행:

`dex --autostart --search-paths `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더3</span>`:`

- GNOME 특정 자동 시작에서 실행될 프로그램 미리보기:

`dex --autostart --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GNOME</span>

- 일반 자동 시작에서 실행될 프로그램 미리보기:

`dex --autostart --dry-run`

- DesktopEntry 속성 `Name`의 값 미리보기:

`dex --property `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.desktop</span>

- 현재 디렉토리에서 프로그램에 대한 DesktopEntry 생성:

`dex --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.desktop</span>

- 주어진 터미널에서 단일 프로그램 실행 (`Terminal=true`가 데스크탑 파일에 있는 경우):

`dex --term `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">터미널</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.desktop</span>
