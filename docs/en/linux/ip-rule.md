---
layout: page
title: linux/ip-rule (English)
description: "IP routing policy database management."
content_hash: 733fcf247bd68611c1b34a5b8e3be748f8233bd3
---
# ip rule

IP routing policy database management.
More information: <https://man7.org/linux/man-pages/man8/ip-rule.8.html>.

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
