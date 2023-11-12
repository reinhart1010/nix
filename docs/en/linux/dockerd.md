---
layout: page
title: linux/dockerd (English)
description: "A persistent process to start and manage docker containers."
content_hash: fcee22fbb061c76f7906e5ae35eeffe8def19e31
last_modified_at: 2023-11-12
related_topics:
  - title: العربية version
    url: /ar/linux/dockerd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dockerd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dockerd

A persistent process to start and manage docker containers.
More information: <https://docs.docker.com/engine/reference/commandline/dockerd/>.

- Run docker daemon:

`dockerd`

- Run docker daemon and config it to listen to specific sockets (UNIX and TCP):

`dockerd --host unix://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/tmp.sock</span>` --host tcp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>

- Run with specific daemon PID file:

`dockerd --pidfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pid_file</span>

- Run in debug mode:

`dockerd --debug`

- Run and set a specific log level:

`dockerd --log-level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug|info|warn|error|fatal</span>
