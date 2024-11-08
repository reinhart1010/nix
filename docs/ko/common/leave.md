---
layout: page
title: common/leave (한국어)
description: "출발할 시간이 되었을 때 알림을 설정."
content_hash: 48bbf9b1e9a7121f97024bac324fb4bb233e1c95
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/leave.html
    icon: bi bi-globe
tldri18n_status: 2
---
# leave

출발할 시간이 되었을 때 알림을 설정.
알림을 제거하려면 `kill $(pidof leave)` 사용.
더 많은 정보: <https://www.freebsd.org/cgi/man.cgi?query=leave>.

- 지정된 시간에 알림 설정:

`leave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출발_시간</span>

- 정오에 출발할 알림 설정:

`leave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1200</span>

- 특정 시간 후에 알림 설정:

`leave +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간_량</span>

- 4시간 4분 후에 출발할 알림 설정:

`leave +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0404</span>
