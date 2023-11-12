---
layout: page
title: common/pamixer (English)
description: "A simple command-line mixer for PulseAudio."
content_hash: 5af1074b9653c92d94ee91a477400f4e06299972
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pamixer

A simple command-line mixer for PulseAudio.
More information: <https://github.com/cdemoulins/pamixer>.

- List all sinks and sources with their corresponding IDs:

`pamixer --list-sinks --list-sources`

- Set the volume to 75% on the default sink:

`pamixer --set-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">75</span>

- Toggle mute on a sink other than the default:

`pamixer --toggle-mute --sink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID</span>

- Increase the volume on default sink by 5%:

`pamixer --increase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Decrease the volume on a source by 5%:

`pamixer --decrease `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID</span>

- Use the allow boost option to increase, decrease, or set the volume above 100%:

`pamixer --set-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">105</span>` --allow-boost`

- Mute the default sink (use `--unmute` instead to unmute):

`pamixer --mute`
