---
layout: page
title: linux/enum4linux (English)
description: "Tool for enumerating Windows and Samba information from remote systems."
content_hash: 63f51376b894ca410535f66ceca6222610d78017
---
# enum4linux

Tool for enumerating Windows and Samba information from remote systems.
It attempts to offer similar functionality to enum.exe formerly available from www.bindview.com.
More information: <https://labs.portcullis.co.uk/tools/enum4linux/>.

- Try to enumerate using all methods:

`enum4linux -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>

- Enumerate using given login credentials:

`enum4linux -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_name</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>

- List usernames from a given host:

`enum4linux -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>

- List shares:

`enum4linux -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>

- Get OS information:

`enum4linux -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>
