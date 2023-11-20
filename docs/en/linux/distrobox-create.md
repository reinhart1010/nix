---
layout: page
title: linux/distrobox-create (English)
description: "Create a distrobox container. See also: `tldr distrobox`."
content_hash: 66101a81859a0ce7e722e54353d256a9545f9cf5
last_modified_at: 2023-11-20
related_topics:
  - title: Nederlands version
    url: /nl/linux/distrobox-create.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-create.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/distrobox-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-create

Create a distrobox container. See also: `tldr distrobox`.
The container created will be tightly integrated with the host, allowing sharing of the user's HOME directory, external storage, external USB devices, graphical apps (X11/Wayland), and audio.
More information: <https://distrobox.it/usage/distrobox-create>.

- Create a distrobox container using the Ubuntu image:

`distrobox-create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubuntu:latest</span>

- Clone a distrobox container:

`distrobox-create --clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cloned_container_name</span>
