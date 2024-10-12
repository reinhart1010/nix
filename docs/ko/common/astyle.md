---
layout: page
title: common/astyle (한국어)
description: "C, C ++, C # 및 Java 프로그래밍 언어에 대한 소스 코드 인덴터, 포맷터 및 미화기."
content_hash: 672b5208228230568d44a7fae0e2f08a2f5c3e1a
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/astyle.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/astyle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/astyle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/astyle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# astyle

C, C ++, C # 및 Java 프로그래밍 언어에 대한 소스 코드 인덴터, 포맷터 및 미화기.
실행 시 원본 파일의 사본은 원래 파일 이름에 ".orig"가 추가된 상태로 작성된다.
더 많은 정보: <https://astyle.sourceforge.net>.

- 들여쓰기 당 4개의 공백의 기본 스타일을 적용하고 형식 변경 없도록 적용:

`astyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스파일명</span>

- Java 스타일 코드로 적용:

`astyle --style=java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>

- allman 스타일 코드로 적용:

`astyle --style=allman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>

- 공간을 사용하여 사용자 지정 들여쓰기를 적용합니다. 2에서 20개 사이의 공간을 선택합니다:

`astyle --indent=spaces=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">띄어쓸_수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>

- 탭을 사용하여 사용자 지정 들여쓰기를 적용합니다. 2에서 20 탭 사이에서 선택합니다:

`astyle --indent=tab=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">탭_수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>
