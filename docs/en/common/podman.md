---
layout: page
title: common/podman (English)
description: "Simple management tool for pods, containers and images."
content_hash: 949ab0668134222a9d3463380e7574b9df058125
related_topics:
  - title: தமிழ் version
    url: /ta/common/podman.html
    icon: bi bi-globe
---
# podman

Simple management tool for pods, containers and images.
Podman provides a Docker-CLI comparable command-line. Simply put: `alias docker=podman`.
More information: <https://github.com/containers/podman/blob/main/commands-demo.md>.

- List all containers (both running and stopped):

`podman ps --all`

- Create a container from an image, with a custom name:

`podman run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Start or stop an existing container:

`podman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Pull an image from a registry (defaults to Docker Hub):

`podman pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Display the list of already downloaded images:

`podman images`

- Open a shell inside an already running container:

`podman exec --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- Remove a stopped container:

`podman rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Display the logs of one or more containers and follow log output:

`podman logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_id</span>
