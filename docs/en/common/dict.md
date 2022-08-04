---
layout: page
title: common/dict (English)
description: "Command line dictionary using the DICT protocol."
content_hash: d5e6610ae7e3c0596377f93e954e0715033f95e2
---
# dict

Command line dictionary using the DICT protocol.
More information: <https://github.com/cheusov/dictd>.

- List available databases:

`dict -D`

- Get information about a database:

`dict -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- Look up a word in a specific database:

`dict -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">word</span>

- Look up a word in all available databases:

`dict `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">word</span>

- Show information about the DICT server:

`dict -I`
