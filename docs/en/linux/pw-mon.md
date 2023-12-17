---
layout: page
title: linux/pw-mon (English)
description: "Monitor objects on the PipeWire instance."
content_hash: c0ad0fc5333b9b7a6709cd3be219b2ff0b5b23d9
last_modified_at: 2023-12-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-mon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-mon

Monitor objects on the PipeWire instance.
More information: <https://docs.pipewire.org/page_man_pw-mon_1.html>.

- Monitor the default PipeWire instance:

`pw-mon`

- Monitor a specific remote instance:

`pw-mon --remote=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Monitor the default instance specifying a color configuration:

`pw-mon --color=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">never|always|auto</span>

- Display help:

`pw-mon --help`
