---
layout: page
title: linux/unshadow (English)
description: "Utility provided by the John the Ripper project to obtain the traditional Unix password file if the system uses shadow passwords."
content_hash: d6ad38805d71a181fca0adf4f5860576a768d977
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# unshadow

Utility provided by the John the Ripper project to obtain the traditional Unix password file if the system uses shadow passwords.
More information: <https://www.openwall.com/john/>.

- Combine the `/etc/shadow` and `/etc/passwd` of the current system:

`sudo unshadow /etc/passwd /etc/shadow`

- Combine two arbitrary shadow and password files:

`sudo unshadow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/passwd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shadow</span>
