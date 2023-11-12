---
layout: page
title: common/adb (English)
description: "Android Debug Bridge: communicate with an Android emulator instance or connected Android devices."
content_hash: 1bce9d36231a15a2aa8c483ec240716aab18a4ea
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/adb.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/adb.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb

Android Debug Bridge: communicate with an Android emulator instance or connected Android devices.
Some subcommands such as `adb shell` have their own usage documentation.
More information: <https://developer.android.com/studio/command-line/adb>.

- Check whether the adb server process is running and start it:

`adb start-server`

- Terminate the adb server process:

`adb kill-server`

- Start a remote shell in the target emulator/device instance:

`adb shell`

- Push an Android application to an emulator/device:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apk</span>

- Copy a file/directory from the target device:

`adb pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local_destination_directory</span>

- Copy a file/directory to the target device:

`adb push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local_file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_destination_directory</span>

- Get a list of connected devices:

`adb devices`
