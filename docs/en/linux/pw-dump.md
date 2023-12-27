---
layout: page
title: linux/pw-dump (English)
description: "Dump PipeWire's current state as JSON, including the information on nodes, devices, modules, ports, and other objects."
content_hash: 3f69f59ec8c41074a661924bc405610493c45e35
last_modified_at: 2023-12-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-dump.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-dump

Dump PipeWire's current state as JSON, including the information on nodes, devices, modules, ports, and other objects.
See also: `pw-mon`.
More information: <https://docs.pipewire.org/page_man_pw-dump_1.html>.

- Print a JSON representation of the default PipeWire instance's current state:

`pw-dump`

- Dump the current state [m]onitoring changes, printing it again:

`pw-dump --monitor`

- Dump the current state of a [r]emote instance to a file:

`pw-dump --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dump_file.json</span>

- Set a [C]olor configuration:

`pw-dump --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">never|always|auto</span>

- Display help:

`pw-dump --help`
