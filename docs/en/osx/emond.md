---
layout: page
title: osx/emond (English)
description: "Event Monitor service that accepts events from various services, runs them through a simple rules engine, and takes action."
content_hash: cd71cc330a0ed1986c8df1048e9d0620dedb1225
---
# emond

Event Monitor service that accepts events from various services, runs them through a simple rules engine, and takes action.
The actions can run commands, send email, or SMS messages.
More information: <https://www.manpagez.com/man/8/emond/>.

- Start the daemon:

`emond`

- Specify rules for emond to process by giving a path to a file or directory:

`emond -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Use a specific configuration file:

`emond -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config</span>
