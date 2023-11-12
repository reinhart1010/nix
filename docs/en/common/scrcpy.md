---
layout: page
title: common/scrcpy (English)
description: "Display and control your Android device on a desktop."
content_hash: 390cfb05b47c5d9e2bbb43b07b73cee076b4c006
last_modified_at: 2023-11-12
related_topics:
  - title: Indonesia version
    url: /id/common/scrcpy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scrcpy

Display and control your Android device on a desktop.
More information: <https://github.com/Genymobile/scrcpy>.

- Display a mirror of a connected device:

`scrcpy`

- Display a mirror of a specific device based on its ID or IP address (find it under the `adb devices` command):

`scrcpy --serial `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0123456789abcdef|192.168.0.1:5555</span>

- Start display in fullscreen mode:

`scrcpy --fullscreen`

- Rotate the display screen. Each incremental value adds a 90 degree counterclockwise rotation:

`scrcpy --rotation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2|3</span>

- Show touches on physical device:

`scrcpy --show-touches`

- Record display screen:

`scrcpy --record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mp4</span>

- Set target directory for pushing files to device by drag and drop (non-APK):

`scrcpy --push-target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
