---
layout: page
title: common/noti (English)
description: "Monitor a process and trigger a banner notification."
content_hash: c3cf95c3250b4bab88addc464d79e1d1ccfd35c3
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# noti

Monitor a process and trigger a banner notification.
More information: <https://github.com/variadico/noti>.

- Display a notification when tar finishes compressing files:

`noti `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tar -cjf example.tar.bz2 example/</span>

- Display a notification even when you put it after the command to watch:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_to_watch</span>`; noti`

- Monitor a process by PID and trigger a notification when the PID disappears:

`noti -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id</span>
