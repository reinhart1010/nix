---
layout: page
title: common/chronic (한국어)
description: "명령이 실패한 경우에만 명령의 `stdout` 및 `stderr`를 표시."
content_hash: 1a383449b9452d5845f21cc0bf082b17d6b0cc51
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/chronic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chronic

명령이 실패한 경우에만 명령의 `stdout` 및 `stderr`를 표시.
더 많은 정보: <https://joeyh.name/code/moreutils/>.

- 0이 아닌 종료 코들드를 생성하거나 충돌하는 경우에만 지정된 명령의 `stdout` 및 `stderr`을 표시:

`chronic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어 옵션 ...</span>

- 비어있지 않은 `stderr`을 생성하는 경우에만 지정된 명령의 `stdout` 및 `stderr`을 표시:

`chronic -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어 옵션 ...</span>

- 상세([v]erbose) 모드 활성화:

`chronic -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어 옵션 ...</span>
