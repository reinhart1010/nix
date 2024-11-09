---
layout: page
title: linux/aa-complain (한국어)
description: "AppArmor 정책을 컴플레인 모드로 설정합니다."
content_hash: 7c3da5a24afb427a1540871d9acbd273b810b5e6
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/linux/aa-complain.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aa-complain.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aa-complain.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/aa-complain.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-complain

AppArmor 정책을 컴플레인 모드로 설정합니다.
같이 보기: `aa-disable`, `aa-enforce`, `aa-status`.
더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-complain.8>.

- 정책을 컴플레인 모드로 설정:

`sudo aa-complain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로필1 경로/대상/프로필2 ...</span>

- 정책들을 컴플레인 모드로 설정:

`sudo aa-complain --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로필들</span>
