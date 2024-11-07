---
layout: page
title: common/r (한국어)
description: "R 언어 인터프리터."
content_hash: 322283075d45ae0f1bd583e3bb8faf869fa2b707
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/r.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/r.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/r.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/r.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># R

R 언어 인터프리터.
더 많은 정보: <https://www.r-project.org>.

- REPL(대화형 셸) 시작:

`R`

- 바닐라 모드에서 R 시작 (즉, 작업 공간을 저장하지 않는 빈 세션):

`R --vanilla`

- 파일 실행:

`R -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.R</span>

- R 표현식을 실행한 후 종료:

`R -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식</span>

- 디버거와 함께 R 실행:

`R -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디버거</span>

- 패키지 소스에서 R 패키지 검사:

`R CMD check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지_소스</span>

- 버전 표시:

`R --version`
