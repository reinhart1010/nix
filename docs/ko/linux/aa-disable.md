---
layout: page
title: linux/aa-disable (한국어)
description: "AppArmor 보안 정책 비활성화."
content_hash: 3f557688159231505e0b74430957c68a4feb79a0
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/aa-disable.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aa-disable.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/aa-disable.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aa-disable.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-disable

AppArmor 보안 정책 비활성화.
같이 보기: `aa-complain`, `aa-enforce`, `aa-status`.
더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- 프로필 비활성화:

`sudo aa-disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로필1 경로/대상/프로필2 ...</span>

- 디렉토리 내의 프로필 비활성화 (기본값은 `/etc/apparmor.d`):

`sudo aa-disable --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로필들</span>
