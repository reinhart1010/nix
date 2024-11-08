---
layout: page
title: common/pee (한국어)
description: "`stdin`을 파이프로 전달하는 도구."
content_hash: 0626c394add7585cf635490e9d1a8f90f6884a0f
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pee.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pee

`stdin`을 파이프로 전달하는 도구.
같이 보기: `tee`.
더 많은 정보: <https://joeyh.name/code/moreutils/>.

- 각 명령을 실행하고, 각 명령에 `stdin`의 별도 복사본 제공:

`pee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령1 명령2 ...</span>

- `stdin`의 복사본을 `stdout`에 쓰기 (`tee`처럼 동작):

`pee cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령1 명령2 ...</span>

- SIGPIPE 및 쓰기 오류 발생 시 즉시 종료:

`pee --no-ignore-sigpipe --no-ignore-write-errors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령1 명령2 ...</span>
