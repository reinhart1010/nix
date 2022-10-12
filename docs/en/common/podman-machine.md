---
layout: page
title: common/podman-machine (English)
description: "Create and manage virtual machines running Podman."
content_hash: 10323f3359954fa6bbb9b8866c1ad9b251337148
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># podman machine

Create and manage virtual machines running Podman.
Included with Podman version 4 or greater.
More information: <https://docs.podman.io/en/latest/markdown/podman-machine.1.html>.

- List existing machines:

`podman machine ls`

- Create a new default machine:

`podman machine init`

- Create a new machine with a specific name:

`podman machine init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Create a new machine with different resources:

`podman machine init --cpus=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --memory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` --disk-size=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>

- Start or stop a machine:

`podman machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Connect to a running machine via SSH:

`podman machine ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Inspect information about a machine:

`podman machine inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
