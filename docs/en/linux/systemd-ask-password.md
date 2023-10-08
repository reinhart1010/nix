---
layout: page
title: linux/systemd-ask-password (English)
description: "Query the user for a system password."
content_hash: b6e6dc44e5220721a7cae8cf41e6dbefec1a5267
last_modified_at: 2023-10-08
---
# systemd-ask-password

Query the user for a system password.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-ask-password.html>.

- Query a system password with a specific message:

`systemd-ask-password "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- Specify an identifier for the password query:

`systemd-ask-password --id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identifier</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- Use a kernel keyring key name as a cache for the password:

`systemd-ask-password --keyname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- Set a custom timeout for the password query:

`systemd-ask-password --timeout=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- Force the use of an agent system and never ask on current TTY:

`systemd-ask-password --no-tty "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- Store a password in the kernel keyring without displaying it:

`systemd-ask-password --no-output --keyname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`
