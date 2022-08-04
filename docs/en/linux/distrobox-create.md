---
layout: page
title: linux/distrobox-create (English)
description: "Create Distrobox containers with an input name and image."
content_hash: 537e5f2f1e615d0b2c287cc884c3fcf0e6197c93
---
# distrobox-create

Create Distrobox containers with an input name and image.
The created container will be tightly integrated with the host, allowing sharing of the HOME directory of the user, external storage, external usb devices and graphical apps (X11/Wayland), and audio.
More information: <https://distrobox.privatedns.org>.

- Create a distrobox using the Alpine image:

`distrobox-create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --image alpine`

- Clone a distrobox:

`distrobox-create --clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cloned_container_name</span>
