---
layout: page
title: linux/cockpit-desktop (English)
description: "Provides secure access to Cockpit pages in an already running session."
content_hash: 80c5a853ae1fa8e5a8d9af9e5af296b28af70149
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cockpit-desktop

Provides secure access to Cockpit pages in an already running session.
It starts `cockpit-ws` and a web browser in an isolated network space and a `cockpit-bridge` in a running user session.
More information: <https://cockpit-project.org/guide/latest/cockpit-desktop.1.html>.

- Open a page:

`cockpit-desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SSH_host</span>

- Open storage page:

`cockpit-desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/cockpit/@localhost/storage/index.html</span>
