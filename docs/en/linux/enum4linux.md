---
layout: page
title: linux/enum4linux (English)
description: "Tool for enumerating Windows and Samba information from remote systems."
content_hash: 576499d242b98705cf7eebab317c82f749dffe7e
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/linux/enum4linux.html
    icon: bi bi-globe
tldri18n_status: 2
---
# enum4linux

Tool for enumerating Windows and Samba information from remote systems.
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
