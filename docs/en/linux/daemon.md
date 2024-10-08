---
layout: page
title: linux/daemon (English)
description: "Run processes into daemons."
content_hash: 8b7161b9799407b007c19ccd1686688e12398564
last_modified_at: 2024-09-09
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/daemon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# daemon

Run processes into daemons.
More information: <https://manned.org/daemon>.

- Run a command as a daemon:

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run a command as a daemon which will restart if the command crashes:

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`" --respawn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run a command as a daemon which will restart if it crashes, with two attempts every 10 seconds:

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`" --respawn --attempts=2 --delay=10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run a command as a daemon, writing logs to a specific file:

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`" --errlog=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.log</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Kill a daemon (SIGTERM):

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`" --stop`

- List daemons:

`daemon --list`
