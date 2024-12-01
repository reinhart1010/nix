---
layout: page
title: common/incus (English)
description: "Modern, secure and powerful system container and virtual machine manager."
content_hash: 8284f4c4e5049d20b8351dd43426014c56078f93
last_modified_at: 2024-12-01
tldri18n_status: 2
---
# incus

Modern, secure and powerful system container and virtual machine manager.
More information: <https://linuxcontainers.org/incus/docs/main>.

- List all containers and virtual machines (both running and stopped):

`incus list`

- Create a container from an image, with a custom name:

`incus create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Start or stop an existing container:

`incus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Open a shell inside an already running container:

`incus shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Remove a stopped container:

`incus delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Pull an image from an image repository (remote) to local:

`incus copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>` local:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom_image_name</span>

- List all available images in the official `images:` remote:

`incus image list images:`

- List all images already downloaded to the `local:` remote:

`incus image list local:`
