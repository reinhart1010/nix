---
layout: page
title: linux/wpctl (English)
description: "Manage WirePlumber, a session and policy manager for PipeWire."
content_hash: f0216c4b3c8032815d512dbcf26c1c73e53a1c98
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# wpctl

Manage WirePlumber, a session and policy manager for PipeWire.
Note: you can use the special name `@DEFAULT_SINK@` in place of `id` to operate on the default sink.
More information: <https://pipewire.pages.freedesktop.org/wireplumber/>.

- List all objects managed by WirePlumber:

`wpctl status`

- Print all properties of an object:

`wpctl inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Set an object to be the default in its group:

`wpctl set-default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Get the volume of a sink:

`wpctl get-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Set the volume of a sink to `n` percent:

`wpctl set-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>`%`

- Increase/Decrease the volume of a sink by `n` percent:

`wpctl set-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>`%`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-</span>

- Mute/Unmute a sink (1 is mute, 0 is unmute):

`wpctl set-mute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|0|toggle</span>
