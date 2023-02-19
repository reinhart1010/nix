---
layout: page
title: common/adb-shell (English)
description: "Android Debug Bridge Shell: Run remote shell commands on an Android emulator instance or connected Android devices."
content_hash: 97ffb25221e05349ec906bd9ad5496e4d95b8633
last_modified_at: 2023-02-19
related_topics:
  - title: français version
    url: /fr/common/adb-shell.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-shell.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-shell.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-shell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-shell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-shell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-shell.html
    icon: bi bi-globe
---
# adb shell

Android Debug Bridge Shell: Run remote shell commands on an Android emulator instance or connected Android devices.
More information: <https://developer.android.com/studio/command-line/adb>.

- Start a remote interactive shell on the emulator or device:

`adb shell`

- Get all the properties from emulator or device:

`adb shell getprop`

- Revert all runtime permissions to their default:

`adb shell pm reset-permissions`

- Revoke a dangerous permission for an application:

`adb shell pm revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">permission</span>

- Trigger a key event:

`adb shell input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keycode</span>

- Clear the data of an application on an emulator or device:

`adb shell pm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Start an activity on emulator or device:

`adb shell am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">activity</span>

- Start the home activity on an emulator or device:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
