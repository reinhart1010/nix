---
layout: page
title: common/tee (한국어)
description: "`stdin`에서 읽고 `stdout` 및 파일(또는 명령어)로 쓰기."
content_hash: 159cd7eb91e7815061430131e34f62b998bbd25d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/tee.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tee.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tee.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tee.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tee

`stdin`에서 읽고 `stdout` 및 파일(또는 명령어)로 쓰기.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html>.

- `stdin`을 각 파일과 `stdout`으로 복사:

`echo "example" | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 주어진 파일에 덧붙이기, 덮어쓰지 않음:

`echo "example" | tee -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`을 터미널에 출력하고, 다른 프로그램으로 파이프하여 추가 처리:

`echo "example" | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xargs printf "[%s]"</span>

- "example"이라는 디렉터리 만들기, "example"의 문자 수 세기, "example"을 터미널에 쓰기:

`echo "example" | tee >(xargs mkdir) >(wc -c)`
