---
layout: page
title: common/tcc (한국어)
description: "C 소스 파일을 스크립트처럼 실행할 수 있는 작은 C 컴파일러로, `gcc`와 유사한 명령줄 옵션을 제공합니다."
content_hash: 6d2a3555f69f07ba9c8fec87db308d116438bcea
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tcc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tcc

C 소스 파일을 스크립트처럼 실행할 수 있는 작은 C 컴파일러로, `gcc`와 유사한 명령줄 옵션을 제공합니다.
더 많은 정보: <https://bellard.org/tcc/tcc-doc.html>.

- 두 개의 소스 파일을 컴파일하고 링크하여 실행 파일 생성:

`tcc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_파일_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.c</span>

- 입력 파일을 스크립트처럼 직접 실행하고 인자를 전달:

`tcc -run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인자들</span>

- 파일 내에 shebang을 사용하여 C 소스 파일 해석:

`#!`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/전체/경로/대상/tcc</span>` -run`
