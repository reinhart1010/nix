---
layout: page
title: linux/dirb (English)
description: "Scan HTTP-based webservers for directories and files."
content_hash: 6f3a719e6d9c861fe9ac4c6867c1b09873cbc0b5
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# dirb

Scan HTTP-based webservers for directories and files.
More information: <https://dirb.sourceforge.net>.

- Scan a webserver using the default wordlist:

`dirb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>

- Scan a webserver using a custom wordlist:

`dirb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wordlist.txt</span>

- Scan a webserver non-recursively:

`dirb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>` -r`

- Scan a webserver using a specified user-agent and cookie for HTTP-requests:

`dirb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_agent_string</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cookie_string</span>
