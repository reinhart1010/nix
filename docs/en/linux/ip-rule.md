---
layout: page
title: linux/ip-rule (English)
description: "IP routing policy database management."
content_hash: 06fe3da04c07e9042b30a75a515d031bd638ff4f
last_modified_at: 2024-06-18
related_topics:
  - title: Türkçe version
    url: /tr/linux/ip-rule.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip rule

IP routing policy database management.
More information: <https://manned.org/ip-rule>.

- Display the routing policy:

`ip rule `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show|list</span>

- Add a new rule based on packet source addresses:

`sudo ip rule add from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- Add a new rule based on packet destination addresses:

`sudo ip rule add to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- Delete a rule based on packet source addresses:

`sudo ip rule delete from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- Delete a rule based on packet destination addresses:

`sudo ip rule delete to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- Flush all deleted rules:

`ip rule flush`

- Save all rules to a file:

`ip rule save > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ip_rules.dat</span>

- Restore all rules from a file:

`ip rule restore < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ip_rules.dat</span>
