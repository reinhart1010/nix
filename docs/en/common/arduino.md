---
layout: page
title: common/arduino (English)
description: "Arduino Studio - Integrated Development Environment for the Arduino platform."
content_hash: d1c555f75e2733b1481acfb74280e05c3e0c39f3
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/arduino.html
    icon: bi bi-globe
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
