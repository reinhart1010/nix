---
layout: page
title: common/particle (English)
description: "Interact with Particle devices."
content_hash: 955ee7ac78070d9e7442a2520b4988f4de257a05
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# particle

Interact with Particle devices.
More information: <https://docs.particle.io/tutorials/developer-tools/cli>.

- Log in or create an account for the Particle CLI:

`particle setup`

- Display a list of devices:

`particle list`

- Create a new Particle project interactively:

`particle project create`

- Compile a Particle project:

`particle compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_code.ino</span>

- Update a device to use a specific app remotely:

`particle flash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/program.bin</span>

- Update a device to use the latest firmware via serial:

`particle flash --serial `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/firmware.bin</span>

- Execute a function on a device:

`particle call `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">function_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">function_arguments</span>
