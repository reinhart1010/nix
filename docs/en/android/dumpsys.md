---
layout: page
title: android/dumpsys (English)
description: "Provide information about Android system services."
content_hash: 2420ae2ce07b550a4de3962ed016951569881f13
related_topics:
  - title: Deutsch version
    url: /de/android/dumpsys.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/dumpsys.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/dumpsys.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/dumpsys.html
    icon: bi bi-globe
  - title: o‘zbek version
    url: /uz/android/dumpsys.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/dumpsys.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/dumpsys.html
    icon: bi bi-globe
---
# dumpsys

Provide information about Android system services.
This command can only be used through `adb shell`.
More information: <https://developer.android.com/studio/command-line/dumpsys>.

- Get diagnostic output for all system services:

`dumpsys`

- Get diagnostic output for a specific system service:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>

- List all services `dumpsys` can give information about:

`dumpsys -l`

- List service-specific arguments for a service:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>` -h`

- Exclude a specific service from the diagnostic output:

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>

- Specify a timeout period in seconds (defaults to 10s):

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>
