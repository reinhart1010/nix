---
layout: page
title: linux/burpsuite (English)
description: "A GUI based application mainly used in web application penetration testing."
content_hash: 35d24d9527633b105125919b557669c8ccca91c3
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># burpsuite

A GUI based application mainly used in web application penetration testing.
More information: <https://portswigger.net/burp/documentation/desktop/getting-started/launch-from-command-line>.

- Start Burp Suite:

`burpsuite`

- Start Burp Suite using the default configuration:

`burpsuite --use-defaults`

- Open a specific project file:

`burpsuite --project-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Load a specific configuration file:

`burpsuite --config-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Start without extensions:

`burpsuite --disable-extensions`