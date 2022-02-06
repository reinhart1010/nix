---
layout: page
title: common/nu (English)
description: "Nushell (\"a new type of shell\") takes a modern, structured approach to your command-line."
content_hash: 05455c9712a1e3563762bb05d0ff586cc0012732
---
# nu

Nushell ("a new type of shell") takes a modern, structured approach to your command-line.
See also: `elvish`.
More information: <https://www.nushell.sh>.

- Start an interactive shell session:

`nu`

- Execute commands:

`nu --commands "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'nu is executed'</span>`"`

- Execute a script:

`nu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.nu</span>

- Execute a script with logging:

`nu --loglevel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">error|warn|info|debug|trace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.nu</span>
