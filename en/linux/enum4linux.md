---
layout: page
title: linux/enum4linux (English)
description: "Tool for enumerating Windows and Samba information from remote systems."
content_hash: 3a18f35d396a14469e74ae910b445e6a1a5052cb
---
# enum4linux

Tool for enumerating Windows and Samba information from remote systems.
It attempts to offer similar functionality to enum.exe formerly available from www.bindview.com.
More information: <https://labs.portcullis.co.uk/tools/enum4linux/>.

- Try to enumerate using all methods:

`enum4linux -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>

- Enumerate using given login credentials:

`enum4liux -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_name</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>

- List usernames from a given host:

`enum4liux -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>

- List shares:

`enum4liux -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>

- Get OS information:

`enum4liux -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>
