---
layout: page
title: common/nxc-vnc (English)
description: "Pentest and exploit VNC servers."
content_hash: 3b37fcded373f6b5021257f9bd904a7ff708a41a
last_modified_at: 2024-10-29
tldri18n_status: 2
---
# nxc vnc

Pentest and exploit VNC servers.
More information: <https://www.netexec.wiki/>.

- Search for valid credentials by trying out every combination in the specified lists of [u]sernames and [p]asswords:

`nxc vnc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/usernames.txt</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/passwords.txt</span>

- Avoid rate limiting through VNC-sleep:

`nxc vnc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{path/to/usernames.txt}</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/passwords.txt</span>` --vnc-sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Take a screenshot on the remote system after waiting the specified amount of time:

`nxc vnc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{username}</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` --screenshot --screentime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
