---
layout: page
title: linux/top (English)
description: "Display dynamic real-time information about running processes."
content_hash: 8e349ca34f9fa52d38ce3911c04bedd212d59944
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/top.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/top.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/top.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/linux/top.html
    icon: bi bi-globe
tldri18n_status: 2
---
# top

Display dynamic real-time information about running processes.
More information: <https://manned.org/top>.

- Start `top`:

`top`

- Do not show any idle or zombie processes:

`top -i`

- Show only processes owned by given user:

`top -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Sort processes by a field:

`top -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_name</span>

- Show the individual threads of a given process:

`top -Hp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id</span>

- Show only the processes with the given PID(s), passed as a comma-separated list. (Normally you wouldn't know PIDs off hand. This example picks the PIDs from the process name):

`top -p $(pgrep -d ',' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>`)`

- Get help about interactive commands:

`?`
