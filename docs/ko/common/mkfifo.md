---
layout: page
title: common/mkfifo (한국어)
description: "FIFO(이름 있는 파이프) 생성."
content_hash: 522c6df497d1e0ee6b3d3533f57baa1b5ed3a393
last_modified_at: 2025-03-02
related_topics:
  - title: bosanski version
    url: /bs/common/mkfifo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/mkfifo.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mkfifo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/mkfifo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfifo

FIFO(이름 있는 파이프) 생성.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html>.

- 지정된 경로에 이름 있는 파이프 생성:

`mkfifo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파이프</span>

- 이름 있는 파이프를 통해 데이터를 보내고 명령을 백그라운드로 전송:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파이프</span>` &`

- 이름 있는 파이프를 통해 데이터 수신:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파이프</span>

- 터미널 세션을 실시간으로 공유:

`mkfifo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파이프</span>`; script -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파이프</span>
