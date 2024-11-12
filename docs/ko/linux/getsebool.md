---
layout: page
title: linux/getsebool (한국어)
description: "SELinux 부울 값 가져오기."
content_hash: 8c027962a76afabdd0048cad3b3f7ece56f10db6
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/getsebool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# getsebool

SELinux 부울 값 가져오기.
같이 보기: `semanage-boolean`, `setsebool`.
더 많은 정보: <https://manned.org/getsebool>.

- 특정 부울의 현재 설정 보기:

`getsebool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd_can_connect_ftp</span>

- 모든 부울의 현재 설정 보기:

`getsebool -a`

- 설명과 함께 모든 부울의 현재 설정 보기:

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>
