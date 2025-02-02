---
layout: page
title: common/lldb (한국어)
description: "LLVM 저수준 디버거."
content_hash: 3132b3908b233473d3de5008ffc85c67b6819697
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/lldb.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/lldb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lldb

LLVM 저수준 디버거.
더 많은 정보: <https://lldb.llvm.org>.

- 실행 파일을 디버그:

`lldb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_파일</span>

- 주어진 PID로 실행 중인 프로세스에 `lldb` 연결:

`lldb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 주어진 이름의 새 프로세스가 시작될 때까지 기다렸다가 연결:

`lldb -w -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>
