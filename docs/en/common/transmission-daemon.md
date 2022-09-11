---
layout: page
title: common/transmission-daemon (English)
description: "Daemon controlled with `transmission-remote` or its web interface."
content_hash: 91e851e05ece7c2548d450b41632bc6047e91525
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># transmission-daemon

Daemon controlled with `transmission-remote` or its web interface.
See also: `transmission`.
More information: <https://manned.org/transmission-daemon>.

- Start a headless `transmission` session:

`transmission-daemon`

- Start and watch a specific directory for new torrents:

`transmission-daemon --watch-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Dump daemon settings in JSON format:

`transmission-daemon --dump-settings > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>

- Start with specific settings for the web interface:

`transmission-daemon --auth --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9091</span>` --allowed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>
