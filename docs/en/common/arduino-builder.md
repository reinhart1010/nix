---
layout: page
title: common/arduino-builder (English)
description: "Compile arduino sketches."
content_hash: d87dae56b7ef66d14e87faa31e3964818a44c2c1
last_modified_at: 2024-08-03
related_topics:
  - title: français version
    url: /fr/common/arduino-builder.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/arduino-builder.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arduino-builder.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arduino-builder

Compile arduino sketches.
DEPRECATION WARNING: this tool is being phased out in favor of `arduino`.
More information: <https://github.com/arduino/arduino-builder>.

- Compile a sketch:

`arduino-builder -compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/sketch.ino</span>

- Specify the debug level (default: 5):

`arduino-builder -debug-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..10</span>

- Specify a custom build directory:

`arduino-builder -build-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build_directory</span>

- Use a build option file, instead of specifying `-hardware`, `-tools`, etc. manually every time:

`arduino-builder -build-options-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build.options.json</span>

- Enable verbose mode:

`arduino-builder -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>
