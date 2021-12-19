---
layout: page
title: common/stdbuf (English)
description: "Run a command with modified buffering operations for its standard streams."
content_hash: 0c2807fc5a5941df61a2914742db6e8a5a6ba3dd
---
# stdbuf

Run a command with modified buffering operations for its standard streams.
More information: <https://www.gnu.org/software/coreutils/stdbuf>.

- Change the standard input buffer size to 512 KiB:

`stdbuf --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512K</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Change the standard output buffer to line-buffered:

`stdbuf --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">L</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Change the standard error buffer to unbuffered:

`stdbuf --error=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
