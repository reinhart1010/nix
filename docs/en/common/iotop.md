---
layout: page
title: common/iotop (English)
description: "Display a table of current I/O usage by processes or threads."
content_hash: 775576eec92771611c2eccad8898e5bf990c440a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# iotop

Display a table of current I/O usage by processes or threads.
More information: <https://manned.org/iotop>.

- Start top-like I/O monitor:

`sudo iotop`

- Show only processes or threads actually doing I/O:

`sudo iotop --only`

- Show I/O usage in non-interactive mode:

`sudo iotop --batch`

- Show only I/O usage of processes (default is to show all threads):

`sudo iotop --processes`

- Show I/O usage of given PID(s):

`sudo iotop --pid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Show I/O usage of a given user:

`sudo iotop --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>

- Show accumulated I/O instead of bandwidth:

`sudo iotop --accumulated`
