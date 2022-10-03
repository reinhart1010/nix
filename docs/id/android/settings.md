---
layout: page
title: android/settings (Indonesia)
description: "Tampilkan informasi terhadap pengaturan sistem operasi Android."
content_hash: 44754fc94051e5141c33ed076685e9ee88738a3f
related_topics:
  - title: Deutsch version
    url: /de/android/settings.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/settings.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/settings.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/settings.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/settings.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/settings.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/settings.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/settings.html
    icon: bi bi-globe
---
# settings

Tampilkan informasi terhadap pengaturan sistem operasi Android.
Informasi lebih lanjut: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Tampilkan daftar pengaturan di dalam namespace `global`:

`settings list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global</span>

- Tampilkan nilai dari pengaturan tertentu:

`settings get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">airplane_mode_on</span>

- Setel nilai pengaturan tertentu:

`settings put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screen_brightness</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- Hapus nilai pengaturan tertentu:

`settings delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secure</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screensaver_enabled</span>
