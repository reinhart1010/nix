---
layout: page
title: linux/fail2ban-client (한국어)
description: "fail2ban 서버를 구성하고 제어."
content_hash: 3cf63eec140814cff36e3bd8d1b6680b9c2504d5
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/fail2ban-client.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fail2ban-client

fail2ban 서버를 구성하고 제어.
더 많은 정보: <https://github.com/fail2ban/fail2ban>.

- 감옥 서비스의 현재 상태 검색:

`fail2ban-client status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">감옥</span>

- 지정된 IP를 감옥 서비스의 차단 목록에서 제거:

`fail2ban-client set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">감옥</span>` unbanip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- fail2ban 서버가 실행 중인지 확인:

`fail2ban-client ping`
