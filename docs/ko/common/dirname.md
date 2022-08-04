---
layout: page
title: common/dirname (한국어)
description: "주어진 파일 혹은 디렉토리 경로의 부모 디렉토리를 계산한다."
content_hash: 3b533258c90827700add1cdbd6fe7f87c4391a20
related_topics:
  - title: English version
    url: /en/common/dirname.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dirname.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dirname.html
    icon: bi bi-globe
---
# dirname

주어진 파일 혹은 디렉토리 경로의 부모 디렉토리를 계산한다.
더 많은 정보: <https://www.gnu.org/software/coreutils/dirname>.

- 주어진 경로의 부모 디렉토리 계산:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일_또는_디렉토리</span>

- 복수 경로의 부모 디렉토리 계산:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/a_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/b_디렉토리</span>

- 개행 대신 NUL 문자로 출력을 구분하기 (`xargs`와 결합 시 유용함):

`dirname --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/a_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/b_파일</span>
