---
layout: page
title: linux/waypipe (English)
description: "Remotely run graphical applications under a Wayland compositor."
content_hash: 4c6625856d9cf4d9140cd040e7c497b1a5bccd14
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/waypipe.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/waypipe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# waypipe

Remotely run graphical applications under a Wayland compositor.
More information: <https://gitlab.freedesktop.org/mstoeckl/waypipe>.

- Run a graphical program remotely and display it locally:

`waypipe ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Open an SSH tunnel to run any program remotely and display it locally:

`waypipe ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>

- Skip testing for Vulkan support:

`waypipe --test-skip-vulkan ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>
