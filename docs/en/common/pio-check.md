---
layout: page
title: common/pio-check (English)
description: "Perform a static analysis check on a PlatformIO project."
content_hash: 9c25bd086eef5683166640af0b3a32e830f867e8
---
# pio check

Perform a static analysis check on a PlatformIO project.
More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_check.html>.

- Perform a basic analysis check on the current project:

`pio check`

- Perform a basic analysis check on a specific project:

`pio check --project-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_dir</span>

- Perform an analysis check for a specific environment:

`pio check --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment</span>

- Perform an analysis check and only report a specified defect severity type:

`pio check --severity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">low|medium|high</span>

- Perform an analysis check and show detailed information when processing environments:

`pio check --verbose`
