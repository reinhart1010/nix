---
layout: page
title: common/stdbuf (English)
description: "Run a command with modified buffering operations for its standard streams."
content_hash: 3858ae3704f1a9b0aa18f01febe49edbb0aaf1a5
last_modified_at: 2024-06-28
tldri18n_status: 2
---
# stdbuf

Run a command with modified buffering operations for its standard streams.
More information: <https://www.gnu.org/software/coreutils/stdbuf>.

- Change `stdin` buffer size to 512 KiB:

`stdbuf --input=512K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Change `stdout` buffer to line-buffered:

`stdbuf --output=L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Change `stderr` buffer to unbuffered:

`stdbuf --error=0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
