---
layout: page
title: linux/last (English)
description: "List information of last user logins."
content_hash: 8b8a3534a33d6103169af0c4eb6fa01c5edf3411
last_modified_at: 2024-04-10
tldri18n_status: 2
---
# last

List information of last user logins.
See also: `lastb`, `login`.
More information: <https://manned.org/last.1>.

- List login information (e.g., username, terminal, boot time, kernel) of all users:

`last`

- List login information of a specific user:

`last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- List information of a specific TTY:

`last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty1</span>

- List most recent information (by default, the newest are at the top):

`last | tac`

- List information of system boots:

`last "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system boot</span>`"`

- List information with a specific [t]imestamp format:

`last --time-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notime|full|iso</span>

- List information [s]ince a specific time and date:

`last --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-7days</span>

- List information (i.e., hostname and IP) of remote hosts:

`last --dns`
