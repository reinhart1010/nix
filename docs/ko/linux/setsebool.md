---
layout: page
title: linux/setsebool (한국어)
description: "SELinux 불리언 값을 설정합니다."
content_hash: d749844b5febf6d72c254201d01a57312992f68a
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/setsebool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# setsebool

SELinux 불리언 값을 설정합니다.
같이 보기: `semanage-boolean`, `getsebool`.
더 많은 정보: <https://manned.org/setsebool>.

- 모든 불리언의 현재 설정을 표시:

`getsebool -a`

- 불리언을 일시적으로 설정 또는 해제 (재부팅 시 비활성화):

`sudo setsebool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd_can_network_connect</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|true|on|0|false|off</span>

- 불리언을 영구적으로 설정 또는 해제:

`sudo setsebool -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_use_devices</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|true|on|0|false|off</span>

- 여러 불리언을 한 번에 영구적으로 설정 또는 해제:

`sudo setsebool -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftpd_use_fusefs=1 mount_anyfile=0 ...</span>

- 불리언을 영구적으로 설정 또는 해제 (대안 방법으로 `semanage-boolean` 사용):

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--modify</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1|--on|-0|--off</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">haproxy_connect_any</span>
