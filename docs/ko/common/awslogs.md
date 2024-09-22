---
layout: page
title: common/awslogs (한국어)
description: "Amazon CloudWatch 로그에서 그룹, 스트림 및 이벤트를 쿼리."
content_hash: 15de1e7b5c8193d0b7d77df352ad063576cf0e72
last_modified_at: 2024-09-22
related_topics:
  - title: Deutsch version
    url: /de/common/awslogs.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/awslogs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# awslogs

Amazon CloudWatch 로그에서 그룹, 스트림 및 이벤트를 쿼리.
더 많은 정보: <https://github.com/jorgebastida/awslogs>.

- 로그 그룹 나열:

`awslogs groups`

- 지정된 그룹의 기존 스트림을 나열:

`awslogs streams `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/syslog</span>

- 1~2시간 전 사이에 지정된 그룹의 모든 스트림에 대한 로그를 가져옴:

`awslogs get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/syslog</span>` --start='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2h ago</span>`' --end='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1h ago</span>`'`

- 특정 CloudWatch Logs 필터 패턴과 일치하는 로그 가져오기:

`awslogs get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/aws/lambda/my_lambda_group</span>` --filter-pattern='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ERROR</span>`'`

- 지정된 그룹의 모든 스트림에 대한 로그를 감시:

`awslogs get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/syslog</span>` ALL --watch`
