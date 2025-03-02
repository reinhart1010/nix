---
layout: page
title: linux/lxc-create (English)
description: "Create linux containers."
content_hash: 24eb748fbbf1d3978a0fa1c32a2b0aa93e358a10
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/lxc-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lxc-create

Create linux containers.
More information: <https://linuxcontainers.org/lxc/getting-started>.

- Create a container interactively in `/var/lib/lxc/`:

`sudo lxc-create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>` --template download`

- Create a container in a target directory:

`sudo lxc-create --lxcpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/directory/</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>` --template download`

- Create a container passing options to a template:

`sudo lxc-create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --template download -- --dist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distro-name</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release-version</span>` --arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arch</span>
