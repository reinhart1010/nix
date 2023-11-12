---
layout: page
title: linux/braa (English)
description: "Ultra-fast mass SNMP scanner allowing multiple hosts simultaneously."
content_hash: 364b1e9f9dd50c21146dfb4dc9a0f3541650b6e6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# braa

Ultra-fast mass SNMP scanner allowing multiple hosts simultaneously.
More information: <https://github.com/mteg/braa>.

- Walk the SNMP tree of host with public string querying all OIDs under `.1.3.6`:

`braa public@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.1.3.6.*</span>

- Query the whole subnet `ip_range` for `system.sysLocation.0`:

`braa public@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_range</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.1.3.6.1.2.1.1.6.0</span>

- Attempt to set the value of `system.sysLocation.0` to a specific workgroup:

`braa private@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.1.3.6.1.2.1.1.6.0</span>`=s'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workgroup</span>`'`
