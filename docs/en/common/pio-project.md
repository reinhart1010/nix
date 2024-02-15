---
layout: page
title: common/pio-project (English)
description: "Manage PlatformIO projects."
content_hash: 102fafc5fa4eb9303ff1a31ac3e135448fbaa9fc
last_modified_at: 2024-02-15
related_topics:
  - title: Nederlands version
    url: /nl/common/pio-project.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio project

Manage PlatformIO projects.
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
