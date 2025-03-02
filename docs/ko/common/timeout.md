---
layout: page
title: common/timeout (한국어)
description: "명령을 일정 시간 제한 내에서 실행."
content_hash: ebd34a1ce2ff3ac6bca70b4f26c597d42771778c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/timeout.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/timeout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# timeout

명령을 일정 시간 제한 내에서 실행.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html>.

- `sleep 10`을 실행하고 3초 후 종료:

`timeout 3s sleep 10`

- 시간 제한이 만료되면 명령에 [s]ignal을 전송 (`TERM`이 기본, 모든 신호 목록은 `kill -l`):

`timeout --signal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INT|HUP|KILL|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sleep 10</span>

- 시간 초과 시 전송된 신호를 `stderr`에 [v]erbose 출력으로 표시:

`timeout --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5s|1m|1h|1d|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 시간 초과 여부와 관계없이 명령의 종료 상태를 유지:

`timeout --preserve-status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1s|1m|1h|1d|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 초기 신호를 무시할 경우 특정 시간 후 강제 `KILL` 신호 전송:

`timeout --kill-after=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
