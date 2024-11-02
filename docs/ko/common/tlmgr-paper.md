---
layout: page
title: common/tlmgr-paper (한국어)
description: "TeX Live 설치의 용지 크기 옵션 관리."
content_hash: 4f36937a7e572f3c4ea38d65bfce9b16cb5310c3
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/tlmgr-paper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tlmgr paper

TeX Live 설치의 용지 크기 옵션 관리.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 모든 TeX Live 프로그램에서 사용되는 기본 용지 크기 표시:

`tlmgr paper`

- 모든 TeX Live 프로그램의 기본 용지 크기를 A4로 설정:

`sudo tlmgr paper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a4</span>

- 특정 TeX Live 프로그램에서 사용되는 기본 용지 크기 표시:

`tlmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdftex</span>` paper`

- 특정 TeX Live 프로그램의 기본 용지 크기를 A4로 설정:

`sudo tlmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdftex</span>` paper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a4</span>

- 특정 TeX Live 프로그램에서 사용 가능한 모든 용지 크기 나열:

`tlmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdftex</span>` paper --list`

- 모든 TeX Live 프로그램에서 사용되는 기본 용지 크기를 JSON 형식으로 출력:

`tlmgr paper --json`
