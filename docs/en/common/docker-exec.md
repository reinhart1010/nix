---
layout: page
title: common/docker-exec (English)
description: "Execute a command on an already running Docker container."
content_hash: bb2201c62200261667e818dd09a98e479f0bbde8
last_modified_at: 2022-12-04
related_topics:
  - title: Deutsch version
    url: /de/common/docker-exec.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-exec.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-exec.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-exec.html
    icon: bi bi-globe
---
# docker exec

Execute a command on an already running Docker container.
More information: <https://docs.docker.com/engine/reference/commandline/exec/>.

- Enter an interactive shell session on an already-running container:

`docker exec --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>

- Run a command in the background (detached) on a running container:

`docker exec --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Select the working directory for a given command to execute into:

`docker exec --interactive -tty --workdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run a command in background on existing container but keep `stdin` open:

`docker exec --interactive --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Set an environment variable in a running Bash session:

`docker exec --interactive --tty --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>

- Run a command as a specific user:

`docker exec --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
