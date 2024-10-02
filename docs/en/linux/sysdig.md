---
layout: page
title: linux/sysdig (English)
description: "System troubleshooting, analysis and exploration."
content_hash: 5e7a2e685ed6372d9b8c1221f2a7c35c888dd740
last_modified_at: 2024-10-02
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sysdig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sysdig

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
