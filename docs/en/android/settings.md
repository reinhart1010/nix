---
layout: page
title: android/settings (English)
description: "Get information about the Android OS."
content_hash: 35c552be36dda30d42ba8a9cab5dc19b019a3e94
related_topics:
  - title: Deutsch version
    url: /de/android/settings.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/settings.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/settings.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/settings.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/settings.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/settings.html
    icon: bi bi-globe
---
# settings

Get information about the Android OS.
More information: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Display a list of settings in the `global` namespace:

`settings list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global</span>

- Get the value of a specific setting:

`settings get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">airplane_mode_on</span>

- Set the value of a setting:

`settings put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screen_brightness</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- Delete a specific setting:

`settings delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secure</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screensaver_enabled</span>
