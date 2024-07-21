---
layout: page
title: common/medusa (English)
description: "A modular and parallel login brute-forcer for a variety of protocols."
content_hash: 4871c76ddce7d5a7ac3cfe2aa072a5fc9f04729f
last_modified_at: 2024-07-21
tldri18n_status: 2
---
# medusa

A modular and parallel login brute-forcer for a variety of protocols.
More information: <https://jmk-foofus.github.io/medusa/medusa.html>.

- List all installed modules:

`medusa -d`

- Show usage example of a specific module (use `medusa -d` for listing all installed modules):

`medusa -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh|http|web-form|postgres|ftp|mysql|...</span>` -q`

- Execute brute force against an FTP server using a file containing usernames and a file containing passwords:

`medusa -M ftp -h host -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/username_file</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/password_file</span>

- Execute a login attempt against an HTTP server using the username, password and user-agent specified:

`medusa -M HTTP -h host -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` -m USER-AGENT:"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Agent</span>`"`

- Execute a brute force against a MySQL server using a file containing usernames and a hash:

`medusa -M mysql -h host -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/username_file</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash</span>` -m PASS:HASH`

- Execute a brute force against a list of SMB servers using a username and a pwdump file:

`medusa -M smbnt -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hosts_file</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pwdump_file</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -m PASS:HASH`
