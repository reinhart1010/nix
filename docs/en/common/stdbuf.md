---
layout: page
title: common/stdbuf (English)
description: "Run a command with modified buffering operations for its standard streams."
content_hash: a4ae9ee8a023fcb397627fe26538c4dce695f899
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# stdbuf

Run a command with modified buffering operations for its standard streams.
More information: <https://www.gnu.org/software/coreutils/stdbuf>.

- Change `stdin` buffer size to 512 KiB:

`stdbuf --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512K</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Change `stdout` buffer to line-buffered:

`stdbuf --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">L</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Change `stderr` buffer to unbuffered:

`stdbuf --error=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
