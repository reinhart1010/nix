---
layout: page
title: osx/lldb (한국어)
description: "LLVM 저수준 디버거."
content_hash: d5f895f58a9c8a9443c4cf7bef7be04c0a7c46ff
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/lldb.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/lldb.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/lldb.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/lldb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lldb

LLVM 저수준 디버거.
더 많은 정보: <https://lldb.llvm.org/man/lldb.html>.

- 실행 파일 디버그:

`lldb "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_파일</span>`"`

- 주어진 PID로 실행 중인 프로세스에 `lldb` 연결:

`lldb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_ID</span>

- 주어진 이름의 새로운 프로세스가 시작될 때까지 기다렸다가 연결:

`lldb -w -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>`"`
