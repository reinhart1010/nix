---
layout: page
title: common/make (한국어)
description: "Makefile에 작성된 대상에 대한 작업 실행기입니다."
content_hash: 4e2d5fdbb826c729561ffe70d1f44b4d924cce24
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/make.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/make.html
    icon: bi bi-globe
tldri18n_status: 2
---
# make

Makefile에 작성된 대상에 대한 작업 실행기입니다.
주로 소스 코드에서 실행 파일의 컴파일을 제어하는 데 사용됩니다.
더 많은 정보: <https://www.gnu.org/software/make/manual/make.html>.

- Makefile에 지정된 첫 번째 대상(일반적으로 "all"이라는 이름)을 호출:

`make`

- 특정 대상을 호출:

`make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 특정 대상을 호출하여, 한 번에 4개의 작업을 병렬로 실행:

`make -j`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 특정 Makefile을 사용:

`make --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 다른 디렉토리에서 make 실행:

`make --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 소스 파일이 변경되지 않은 경우에도, 대상을 강제로 make 실행:

`make --always-make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- Makefile에 정의된 변수를 재정의:

`make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_값</span>

- 환경에 의해 Makefile에 정의된 변수를 재정의:

`make --environment-overrides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>
