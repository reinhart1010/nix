---
layout: page
title: common/trap (한국어)
description: "이벤트 발생 시 명령을 실행."
content_hash: c557626c7c4ce8efbad113350ae82c324fc55714
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/trap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/trap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# trap

이벤트 발생 시 명령을 실행.
더 많은 정보: <https://manned.org/trap.1posix>.

- 예상 이벤트의 이름과 명령 나열:

`trap`

- 신호를 받았을 때 명령 실행:

`trap 'echo "신호 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>` 수신"' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HUP</span>

- 명령 제거:

`trap - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INT</span>
