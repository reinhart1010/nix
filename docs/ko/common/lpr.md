---
layout: page
title: common/lpr (한국어)
description: "파일을 인쇄합니다."
content_hash: 73fca586f37df4f754f0a8cf748e6f71a41aefcd
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/lpr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/lpr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lpr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpr

파일을 인쇄합니다.
같이 보기: `lpstat` 및 `lpadmin`.
더 많은 정보: <https://openprinting.github.io/cups/doc/man-lpr.html>.

- 기본 프린터로 파일 인쇄:

`lpr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 2부 인쇄:

`lpr -# `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정된 프린터로 인쇄:

`lpr -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 페이지(예: 2) 또는 페이지 범위(예: 2-16) 인쇄:

`lpr -o page-ranges=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|2-16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 세로(긴) 또는 가로(짧은) 양면 인쇄:

`lpr -o sides=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">two-sided-long-edge|two-sided-short-edge</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 페이지 크기 설정 (설정에 따라 더 많은 옵션 사용 가능):

`lpr -o media=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a4|letter|legal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 한 장에 여러 페이지 인쇄:

`lpr -o number-up=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|4|6|9|16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
