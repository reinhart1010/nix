---
layout: page
title: common/indent (한국어)
description: "공백을 삽입하거나 삭제하여 a C/C++ 프로그램의 모양을 변경."
content_hash: 7dded88eef5738ba0dea978ea53a5035e4f208b5
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/indent.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/indent.html
    icon: bi bi-globe
tldri18n_status: 2
---
# indent

공백을 삽입하거나 삭제하여 a C/C++ 프로그램의 모양을 변경.
더 많은 정보: <https://www.gnu.org/software/indent/>.

- Linux 스타일 가이드에 따라 C/C++ 소스 형식을 지정하고, 원본 파일을 자동으로 백업한 후, 들여쓰기된 버전으로 변경:

`indent --linux-style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/또다른_소스.c</span>

- GNU 스타일에 따라 C/C++ 소스 형식을 지정하고, 들여쓰기된 버전을 다른 파일에 저장:

`indent --gnu-style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/들여쓰기된_소스.c</span>

- Kernighan & Ritchie (K&R) 스타일에 따라 C/C++ 소스 형식을 지정하고, 탭이 없으며, 들여쓰기당 공백 3개, 줄바꿈은 120자:

`indent --k-and-r-style --indent-level3 --no-tabs --line-length120 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/들여쓰기된_소스.c</span>
