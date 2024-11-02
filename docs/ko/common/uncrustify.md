---
layout: page
title: common/uncrustify (한국어)
description: "C, C++, C#, D, Java 및 Pawn 소스 코드 포매터."
content_hash: 38908c5ded9b6ecd7fb44d37ce724a7f73f35b80
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/uncrustify.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uncrustify

C, C++, C#, D, Java 및 Pawn 소스 코드 포매터.
더 많은 정보: <https://github.com/uncrustify/uncrustify>.

- 단일 파일 포맷팅:

`uncrustify -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cpp</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.cpp</span>

- `stdin`에서 파일 이름을 읽고, 원본 파일 경로에 출력을 다시 쓰기 전에 백업 생성:

`find . -name "*.cpp" | uncrustify -F - --replace`

- 백업 생성 안 함 (파일이 버전 관리 중인 경우 유용):

`find . -name "*.cpp" | uncrustify -F - --no-backup`

- 사용자 지정 설정 파일을 사용하고 결과를 `stdout`에 출력:

`uncrustify -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/uncrustify.cfg</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cpp</span>

- 설정 변수를 명시적으로 설정:

`uncrustify --set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 새 설정 파일 생성:

`uncrustify --update-config -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/new.cfg</span>
