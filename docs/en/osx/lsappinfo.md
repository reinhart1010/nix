---
layout: page
title: osx/lsappinfo (English)
description: "Control and query CoreApplicationServices about the app state on the system."
content_hash: e74bf50138210e3b296fb002a60c22b3f921691f
last_modified_at: 2024-01-03
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/lsappinfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lsappinfo

Control and query CoreApplicationServices about the app state on the system.
More information: <https://keith.github.io/xcode-man-pages/lsappinfo.8.html>.

- List all running applications with their details:

`lsappinfo list`

- Show the front application:

`lsappinfo front`

- Show the information for a specific application:

`lsappinfo info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.calculator</span>
