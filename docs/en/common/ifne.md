---
layout: page
title: common/ifne (English)
description: "Run a command depending on the emptyness of `stdin`."
content_hash: 97f128e35a060e8402a481127e0dda60288331d6
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# ifne

Run a command depending on the emptyness of `stdin`.
More information: <https://joeyh.name/code/moreutils/>.

- Run the specified command if and only if `stdin` is not empty:

`ifne `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command options ...</span>

- Run the specified command if and only if `stdin` is empty, otherwise pass `stdin` to `stdout`:

`ifne -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command options ...</span>
