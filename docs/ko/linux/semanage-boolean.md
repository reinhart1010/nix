---
layout: page
title: linux/semanage-boolean (한국어)
description: "SELinux 부울 설정을 영구적으로 관리합니다."
content_hash: a2716985411b6b885c8bfdcb169fe27574aba0d4
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/semanage-boolean.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/semanage-boolean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# semanage boolean

SELinux 부울 설정을 영구적으로 관리합니다.
같이 보기: SELinux 정책 관리를 위한 `semanage`, 부울 값을 확인하기 위한 `getsebool`, 비영구적 부울 설정 적용을 위한 `setsebool`.
더 많은 정보: <https://manned.org/semanage-boolean>.

- 모든 부울 설정 나열:

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>

- 사용자 정의 부울 설정을 제목 없이 나열:

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-C|--locallist</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--noheading</span>

- 부울을 영구적으로 설정 또는 해제:

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--modify</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1|--on|-0|--off</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">haproxy_connect_any</span>
