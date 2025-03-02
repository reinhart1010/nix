---
layout: page
title: linux/trap (한국어)
description: "이벤트 발생 시 명령을 실행합니다."
content_hash: dde0d9cf75a720cdd6428fa838b27ee9b787c343
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/trap.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># trap

이벤트 발생 시 명령을 실행합니다.
더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-trap>.

- 사용 가능한 이벤트 이름 나열 (예: `SIGWINCH`):

`trap -l`

- 명령과 예상 이벤트 이름 나열:

`trap -p`

- 신호를 받았을 때 명령 실행:

`trap 'echo "Caught signal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>`"' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>

- 명령 제거:

`trap - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGINT</span>
