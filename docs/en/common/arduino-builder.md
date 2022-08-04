---
layout: page
title: common/arduino-builder (English)
description: "A command-line tool for compiling arduino sketches."
content_hash: 5bbea3eeb96b19f791789a94d6fc73b01f5bc249
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/arduino-builder.html
    icon: bi bi-globe
---
# arduino-builder

A command-line tool for compiling arduino sketches.
DEPRECATION WARNING: This tool is being phased out in favor of `arduino`.
More information: <https://github.com/arduino/arduino-builder>.

- Compile a sketch:

`arduino-builder -compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/sketch.ino</span>

- Specify the debug level (1 to 10, defaults to 5):

`arduino-builder -debug-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">level</span>

- Specify a custom build directory:

`arduino-builder -build-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build_directory</span>

- Use a build option file, instead of specifying `--hardware`, `--tools`, etc. manually every time:

`arduino-builder -build-options-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build.options.json</span>

- Enable verbose mode:

`arduino-builder -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>
