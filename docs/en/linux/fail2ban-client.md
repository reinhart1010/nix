---
layout: page
title: linux/fail2ban-client (English)
description: "Configure and control fail2ban server."
content_hash: bfdb44caa3bb3ab01051861367716a0f7ec75180
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# fail2ban-client

Configure and control fail2ban server.
More information: <https://github.com/fail2ban/fail2ban>.

- Retrieve current status of the jail service:

`fail2ban-client status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jail</span>

- Remove the specified IP from the jail service's ban list:

`fail2ban-client set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jail</span>` unbanip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>

- Verify fail2ban server is alive:

`fail2ban-client ping`
