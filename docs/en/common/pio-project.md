---
layout: page
title: common/pio-project (English)
description: "Tool to manage PlatformIO projects."
content_hash: 3a7ac1ee37fe67376ded3cd59a2c4778e9a92832
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pio project

Tool to manage PlatformIO projects.
More information: <https://docs.platformio.org/en/latest/core/userguide/project/>.

- Initialize a new PlatformIO project:

`pio project init`

- Initialize a new PlatformIO project in a specific directory:

`pio project init --project-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_directory</span>

- Initialize a new PlatformIO project, specifying a board ID:

`pio project init --board `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ATmega328P|uno|...</span>

- Initialize a new PlatformIO based project, specifying one or more project options:

`pio project init --project-option="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`" --project-option="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"`

- Print the configuration of a project:

`pio project config`
