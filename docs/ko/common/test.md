---
layout: page
title: common/test (한국어)
description: "파일 유형을 확인하고 값을 비교."
content_hash: ddf6670b82b5252d809b0e9361cebceeb428e114
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/test.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/test.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/test.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/test.html
    icon: bi bi-globe
tldri18n_status: 2
---
# test

파일 유형을 확인하고 값을 비교.
조건이 참이면 0을 반환하고, 거짓이면 1을 반환합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/test-invocation.html>.

- 주어진 변수가 특정 문자열과 같은지 확인:

`test "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$MY_VAR</span>`" = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/zsh</span>`"`

- 주어진 변수가 비어 있는지 확인:

`test -z "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GIT_BRANCH</span>`"`

- 파일이 존재하는지 확인:

`test -f "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>`"`

- 디렉토리가 존재하지 않는지 확인:

`test ! -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>`"`

- A가 참이면 B를 실행하고, 오류가 발생하면 C를 실행 (A가 실패해도 C가 실행될 수 있음):

`test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조건</span>` && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "true"</span>` || `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "false"</span>
