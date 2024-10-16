---
layout: page
title: common/erl (한국어)
description: "Erlang 프로그래밍 언어로 프로그램을 실행하고 관리."
content_hash: a7794e7df688b1e4e8cd81e13c21f857a0d0dbb4
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/erl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/erl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/erl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># erl

Erlang 프로그래밍 언어로 프로그램을 실행하고 관리.
더 많은 정보: <https://www.erlang.org>.

- 순차적 Erlang 프로그램을 공통 스크립트로 컴파일하고 실행한 후 종료:

`erlc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` && erl -noshell '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mymodule:myfunction(arguments)</span>`, init:stop().'`

- 실행중인 Erlang 노드에 연결:

`erl -remsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드이름</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -sname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커스텀_단축이름</span>` -hidden -setcookie `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격노드의_쿠키</span>

- 디렉터리에서 모듈을 로드하도록 Erlang 쉘에 지시:

`erl -pa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/beam파일에_관한_디렉토리</span>
