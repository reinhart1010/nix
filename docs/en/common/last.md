---
layout: page
title: common/last (English)
description: "View the last logged in users."
content_hash: 430481c00b828fac7ae020bacd34d2933b94316b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# last

View the last logged in users.
More information: <https://manned.org/last>.

- View last logins, their duration and other information as read from `/var/log/wtmp`:

`last`

- Specify how many of the last logins to show:

`last -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">login_count</span>

- Print the full date and time for entries and then display the hostname column last to prevent truncation:

`last -F -a`

- View all logins by a specific user and show the IP address instead of the hostname:

`last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -i`

- View all recorded reboots (i.e., the last logins of the pseudo user "reboot"):

`last reboot`

- View all recorded shutdowns (i.e., the last logins of the pseudo user "shutdown"):

`last shutdown`
