---
layout: page
title: common/lpmove (한국어)
description: "작업 또는 모든 작업을 다른 프린터로 이동."
content_hash: 41ab3e3fe42327c088a2ede1f6fb7a6cac4abf52
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/lpmove.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lpmove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpmove

작업 또는 모든 작업을 다른 프린터로 이동.
같이 보기: `cancel`, `lp`, `lpr`, `lprm`.
더 많은 정보: <https://openprinting.github.io/cups/doc/man-lpmove.html>.

- 특정 작업을 `new_printer`로 이동:

`lpmove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_printer</span>

- `old_printer`에서 `new_printer`로 작업 이동:

`lpmove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_printer</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_printer</span>

- `old_printer`에서 `new_printer`로 모든 작업 이동:

`lpmove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_printer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_printer</span>

- 특정 서버에서 `new_printer`로 특정 작업 이동:

`lpmove -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_printer</span>
