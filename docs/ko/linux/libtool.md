---
layout: page
title: linux/libtool (한국어)
description: "공유 라이브러리를 사용하는 복잡성을 일관되고 이식 가능한 인터페이스 뒤로 숨기는 제네릭 라이브러리 지원 스크립트."
content_hash: 4966780157c5a78140d3cad53a5a57706f72b703
last_modified_at: 2024-11-27
related_topics:
  - title: English version
    url: /en/linux/libtool.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/libtool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# libtool

공유 라이브러리를 사용하는 복잡성을 일관되고 이식 가능한 인터페이스 뒤로 숨기는 제네릭 라이브러리 지원 스크립트.
더 많은 정보: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtool>.

- 소스 파일을 `libtool` 객체로 컴파일:

`libtool --mode=compile gcc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본.lo</span>

- 라이브러리 또는 실행 파일 생성:

`libtool --mode=link gcc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/라이브러리.lo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본.lo</span>

- 라이브러리 경로를 자동으로 설정하여 다른 프로그램이 설치되지 않은 `libtool` 생성 프로그램 또는 라이브러리를 사용할 수 있도록 합니다:

`libtool --mode=execute gdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로그램</span>

- 공유 라이브러리 설치:

`libtool --mode=install cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/라이브러리.la</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/설치_디렉토리</span>

- 시스템에서 `libtool` 라이브러리 설치 완료:

`libtool --mode=finish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/설치_디렉토리</span>

- 설치된 라이브러리 또는 실행 파일 삭제:

`libtool --mode=uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/설치된_라이브러리.la</span>

- 설치되지 않은 라이브러리 또는 실행 파일 삭제:

`libtool --mode=clean rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본.lo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/라이브러리.la</span>
