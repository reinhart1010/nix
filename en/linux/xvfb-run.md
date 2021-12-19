---
layout: page
title: linux/xvfb-run (English)
description: "Run a command in a virtual X server environment."
content_hash: ad274b64cf88d1732609f4055b9a662f32c5b8f4
---
# xvfb-run

Run a command in a virtual X server environment.
More information: <https://www.x.org/wiki/>.

- Run the specified command in a virtual X server:

`xvfb-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Try to get a free server number, if the default (99) is not available:

`xvfb-run --auto-servernum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Pass arguments to the Xvfb server:

`xvfb-run --server-args "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-screen 0 1024x768x24</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
