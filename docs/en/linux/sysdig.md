---
layout: page
title: linux/sysdig (English)
description: "System troubleshooting, analysis and exploration."
content_hash: 5e7a2e685ed6372d9b8c1221f2a7c35c888dd740
last_modified_at: 2024-10-03
tldri18n_status: 2
---
# sysdig

System troubleshooting, analysis and exploration.
Capture, filter and store systemcalls.
More information: <https://github.com/draios/sysdig/wiki>.

- Capture all the events from the live system and print them to screen:

`sysdig`

- Capture all the events from the live system and save them to disk:

`sysdig -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.scap`

- Read events from a file and print them to screen:

`sysdig -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.scap`

- Filter and Print all the open system calls invoked by cat:

`sysdig proc.name=cat and evt.type=open`

- Register any found plugin and use dummy as input source passing to it open params:

`sysdig -I dummy:'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parameter</span>`'`

- List the available chisels:

`sysdig -cl`

- Use the spy_ip chisel to look at the data exchanged with ip address:

`sysdig -c spy_ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>
