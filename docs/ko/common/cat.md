---
layout: page
title: common/cat (한국어)
description: "파일 출력 및 연결."
content_hash: ff6718f0bc77a3446649614a5b037ba62f7e2cfa
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cat.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cat.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/cat.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/cat.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cat.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cat

파일 출력 및 연결.
더 많은 정보: <https://www.gnu.org/software/coreutils/cat>.

- 표준출력으로 파일 내용 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- 여러 파일을 대상 파일에 연결:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_파일명</span>

- 대상 파일에 여러 파일 내용 추가:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명2</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_파일명</span>

- 모든 출력 라인에 번호 매기기:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- 출력할 수 없는 문자 및 공백 문자 표시 (ASCII가 아닌 경우 `M-`접두사 포함):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>
