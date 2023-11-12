---
layout: page
title: common/arduino (English)
description: "Arduino Studio - Integrated Development Environment for the Arduino platform."
content_hash: 8baf82bb96578fa43c187badf4396983d23dabaa
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/arduino.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arduino.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arduino

Arduino Studio - Integrated Development Environment for the Arduino platform.
More information: <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

- Build a sketch:

`arduino --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ino</span>

- Build and upload a sketch:

`arduino --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ino</span>

- Build and upload a sketch to an Arduino Nano with an Atmega328p CPU, connected on port `/dev/ttyACM0`:

`arduino --board `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arduino:avr:nano:cpu=atmega328p</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyACM0</span>` --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ino</span>

- Set the preference `name` to a given `value`:

`arduino --pref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Build a sketch, put the build results in the build directory, and reuse any previous build results in that directory:

`arduino --pref build.path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build_directory</span>` --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ino</span>

- Save any (changed) preferences to `preferences.txt`:

`arduino --save-prefs`

- Install the latest SAM board:

`arduino --install-boards "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arduino:sam</span>`"`

- Install Bridge and Servo libraries:

`arduino --install-library "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Bridge:1.0.0,Servo:1.2.0</span>`"`
