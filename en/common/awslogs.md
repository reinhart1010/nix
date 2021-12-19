---
layout: page
title: common/awslogs (English)
description: "Queries groups, streams and events from Amazon CloudWatch logs."
content_hash: 0771ff954bbb581253956c8b932cd687475768be
related_topics:
  - title: Deutsch version
    url: /de/common/awslogs.html
    icon: bi bi-globe
---
# awslogs

Queries groups, streams and events from Amazon CloudWatch logs.
More information: <https://github.com/jorgebastida/awslogs>.

- List log groups:

`awslogs groups`

- List existing streams for the specified group:

`awslogs streams `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/syslog</span>

- Get logs for any streams in the specified group between 1 and 2 hours ago:

`awslogs get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/syslog</span>` --start='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2h ago</span>`' --end='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1h ago</span>`'`

- Get logs that match a specific CloudWatch Logs Filter pattern:

`awslogs get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/aws/lambda/my_lambda_group</span>` --filter-pattern='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ERROR</span>`'`

- Watch logs for any streams in the specified group:

`awslogs get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/syslog</span>` ALL --watch`
