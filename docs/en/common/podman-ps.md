---
layout: page
title: common/podman-ps (English)
description: "List Podman containers."
content_hash: 5b15dee3db27cb2aa565e4ce05d233c69bef340d
last_modified_at: 2024-03-14
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/podman-ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman ps

List Podman containers.
More information: <https://docs.podman.io/en/latest/markdown/podman-ps.1.html>.

- List currently running Podman containers:

`podman ps`

- List all Podman containers (running and stopped):

`podman ps --all`

- Show the latest created container (includes all states):

`podman ps --latest`

- Filter containers that contain a substring in their name:

`podman ps --filter "name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`"`

- Filter containers that share a given image as an ancestor:

`podman ps --filter "ancestor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>`"`

- Filter containers by exit status code:

`podman ps --all --filter "exited=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`"`

- Filter containers by status (created, running, removing, paused, exited and dead):

`podman ps --filter "status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>`"`

- Filter containers that mount a specific volume or have a volume mounted in a specific path:

`podman ps --filter "volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`" --format "table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ID</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Image</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Names</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Mounts</span>`"`
