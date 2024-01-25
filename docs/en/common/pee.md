---
layout: page
title: common/pee (English)
description: "Tee `stdin` to pipes."
content_hash: af3842329c1a1a3280ecdb1457b27248958214fd
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# pee

Tee `stdin` to pipes.
See also: `tee`.
More information: <https://joeyh.name/code/moreutils/>.

- Run each command, providing each one with a distinct copy of `stdin`:

`pee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1 command2 ...</span>

- Write a copy of `stdin` to `stdout` (like `tee`):

`pee cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1 command2 ...</span>

- Immediately terminate upon SIGPIPEs and write errors:

`pee --no-ignore-sigpipe --no-ignore-write-errors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1 command2 ...</span>
