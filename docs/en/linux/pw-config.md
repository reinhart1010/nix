---
layout: page
title: linux/pw-config (English)
description: "List configuration paths and sections that will be used by the PipeWire server and clients."
content_hash: 81f58526c2e0a72e704f29f20723718a1ee1fb5a
last_modified_at: 2024-05-20
tldri18n_status: 2
---
# pw-config

List configuration paths and sections that will be used by the PipeWire server and clients.
More information: <https://docs.pipewire.org/page_man_pw-config_1.html>.

- List all configuration files that will be used:

`pw-config`

- List all configuration files that will be used by the PipeWire PulseAudio server:

`pw-config --name pipewire-pulse.conf`

- List all configuration sections used by the PipeWire PulseAudio server:

`pw-config --name pipewire-pulse.conf list`

- List the `context.properties` fragments used by the JACK clients:

`pw-config --name jack.conf list context.properties`

- List the merged `context.properties` used by the JACK clients:

`pw-config --name jack.conf merge context.properties`

- List the merged `context.modules` used by the PipeWire server and [r]eformat:

`pw-config --name pipewire.conf --recurse merge context.modules`

- Display help:

`pw-config --help`
