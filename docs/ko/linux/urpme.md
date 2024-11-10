---
layout: page
title: linux/urpme (한국어)
description: "Mageia에서 패키지를 제거합니다."
content_hash: e7aa777698a2dc7668bf6f86f0548b09e493af3f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/urpme.html
    icon: bi bi-globe
tldri18n_status: 2
---
# urpme

Mageia에서 패키지를 제거합니다.
같이 보기: `urpmi`, `urpmi.update`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
더 많은 정보: <https://wiki.mageia.org/en/URPMI#urpme>.

- 패키지 제거:

`sudo urpme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 고아 패키지 제거 (주의: 중요한 패키지가 의도치 않게 제거될 수 있습니다):

`sudo urpme --auto-orphans`

- 패키지 및 의존성 제거:

`sudo urpme --auto-orphans `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
