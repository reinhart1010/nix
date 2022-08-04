---
layout: page
title: linux/lxc-profile (English)
description: "Manage profiles for LXD containers."
content_hash: 3ea9233806057c37722c9460f86098d921b33e9b
---
# lxc profile

Manage profiles for LXD containers.
More information: <https://linuxcontainers.org/lxd/docs/master/profiles>.

- List all available profiles:

`lxc profile list`

- Show the configuration of a specific profile:

`lxc profile show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Edit a specific profile in the default editor:

`lxc profile edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Edit a specific profile importing the configuration values from a file:

`lxc profile edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config.yaml</span>

- Launch a new container with specific profiles:

`lxc launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_image</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile1</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile2</span>

- Change the profiles of a running container:

`lxc profile assign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile1,profile2</span>
