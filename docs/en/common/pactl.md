---
layout: page
title: common/pactl (English)
description: "Control a running PulseAudio sound server."
content_hash: 1cdbf59d117b6523da421900973141514930cfbf
last_modified_at: 2024-05-17
tldri18n_status: 2
---
# pactl

Control a running PulseAudio sound server.
More information: <https://manned.org/pactl>.

- Show information about the sound server:

`pactl info`

- List all sinks (or other types - sinks are outputs and sink-inputs are active audio streams):

`pactl list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sinks</span>` short`

- Change the default sink (output) to 1 (the number can be retrieved via the `list` subcommand):

`pactl set-default-sink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Move sink-input 627 to sink 1:

`pactl move-sink-input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">627</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Set the volume of sink 1 to 75%:

`pactl set-sink-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.75</span>

- Toggle mute on the default sink (using the special name `@DEFAULT_SINK@`):

`pactl set-sink-mute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@DEFAULT_SINK@</span>` toggle`
