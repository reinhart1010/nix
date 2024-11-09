---
layout: page
title: linux/addr2line (한국어)
description: "바이너리의 주소를 파일 이름과 줄 번호로 변환."
content_hash: c4073e274ed6b4b95a2a2a18e2a218595f103cc5
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/linux/addr2line.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/addr2line.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/addr2line.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/addr2line.html
    icon: bi bi-globe
tldri18n_status: 2
---
# addr2line

바이너리의 주소를 파일 이름과 줄 번호로 변환.
더 많은 정보: <https://manned.org/addr2line>.

- 실행 파일의 명령어 주소로부터 소스 코드의 파일 이름과 줄 번호 표시:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>

- 함수 이름, 파일 이름 및 줄 번호 표시:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행_파일</span>` --functions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>

- C++ 코드의 함수 이름 디맹글링:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행_파일</span>` --functions --demangle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>
