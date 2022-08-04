---
layout: page
title: common/pio-debug (English)
description: "Debug PlatformIO projects."
content_hash: 28dce6c899515bc5f09ba676beb5e91ac5bf6294
---
# pio debug

Debug PlatformIO projects.
More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_debug.html>.

- Debug the PlatformIO project in the current directory:

`pio debug`

- Debug a specific PlatformIO project:

`pio debug --project-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/platformio_project</span>

- Debug a specific environment:

`pio debug --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment</span>

- Debug a PlatformIO project using a specific configuration file:

`pio debug --project-conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/platformio.ini</span>

- Debug a PlatformIO project using the `gdb` debugger:

`pio debug --interface=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gdb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gdb_options</span>
