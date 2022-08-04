---
layout: page
title: common/pio-run (English)
description: "Run PlatformIO project targets."
content_hash: 253a3c39795f90bd055f4ebc5b0bd76c0d8b3c7f
---
# pio run

Run PlatformIO project targets.
More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_run.html>.

- List all available project targets:

`pio run --list-targets`

- List all available project targets of a specific environment:

`pio run --list-targets --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment</span>

- Run all targets:

`pio run`

- Run all targets of specified environments:

`pio run --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment1</span>` --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment2</span>

- Run specified targets:

`pio run --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target1</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target2</span>

- Run the targets of a specified configuration file:

`pio run --project-conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/platformio.ini</span>
