---
layout: page
title: common/figlet (한국어)
description: "사용자 입력에서 ASCII 배너를 생성."
content_hash: 113839d5d1a8338e8adee67c19260f6b50687082
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/figlet.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/figlet.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/figlet.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># figlet

사용자 입력에서 ASCII 배너를 생성.
참고: `showfigfonts`.
더 많은 정보: <http://www.figlet.org/figlet-man.html>.

- 텍스트를 직접 입력하여 생성:

`figlet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_문자열</span>

- 사용자 정의 폰트([f]ont) 파일을 사용:

`figlet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_문자열</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폰트_파일.flf</span>

- 기본 글꼴 디렉토리의 폰트([f]ont)를 사용 (확장자는 생략 가능):

`figlet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_문자열</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">폰트_파일이름</span>

- FIGlet을 통한 파이프 명령 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | figlet`

- 사용 가능한 FIGlet 글꼴 표시:

`showfigfonts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표시할 선택적 문자열</span>

- 터미널([t]erminal)의 전체 너비를 사용하고 입력 텍스트를 중앙([c]enter)에 배치:

`figlet -t -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_문자열</span>

- 겹치지 않도록 모든 문자를 전체 너비([W]idth)로 표시:

`figlet -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_문자열</span>
