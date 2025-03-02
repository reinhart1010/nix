---
layout: page
title: common/gdb (한국어)
description: "GNU 디버거."
content_hash: 5f3eb462f4879164c52890d3abf700dd01e03ab0
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/gdb.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gdb.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/gdb.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/gdb.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gdb.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gdb

GNU 디버거.
더 많은 정보: <https://www.gnu.org/software/gdb>.

- 실행파일을 디버깅합니다:

`gdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행파일</span>

- 프로세스를 gdb에 연결합니다:

`gdb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스ID</span>

- 코어 파일과 함께 디버깅합니다:

`gdb -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행파일</span>

- 디버깅을 시작하면서 주어진 GDB 명령들을 수행합니다:

`gdb -ex "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령들</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행파일</span>

- 디버깅을 시작하면서 실행파일에 인자들을 넘겨줍니다:

`gdb --args `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인자1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인자2</span>
