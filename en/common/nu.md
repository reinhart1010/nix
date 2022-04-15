---
layout: page
title: common/nu (English)
description: "Nushell (\"a new type of shell\") takes a modern, structured approach to your command-line."
content_hash: 43015f18967eb3f4a86a33aa9409377daf933216
---
# nu

Nushell ("a new type of shell") takes a modern, structured approach to your command-line.
See also: `elvish`.
More information: <https://www.nushell.sh>.

- Start an interactive shell session:

`nu`

- Execute specific commands:

`nu --commands "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'nu is executed'</span>`"`

- Execute a specific script:

`nu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.nu</span>

- Execute a specific script with logging:

`nu --loglevel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">error|warn|info|debug|trace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.nu</span>
