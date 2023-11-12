---
layout: page
title: android/settings (français)
description: "Récupère les informations du système d'exploitation Android."
content_hash: 6533e7e98b37ddaff9e4bf429d616e3134aa2b71
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/android/settings.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/settings.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/settings.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/settings.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/android/settings.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/android/settings.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/settings.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/android/settings.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/android/settings.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/settings.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/settings.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/settings.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/settings.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/settings.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/settings.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/android/settings.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/settings.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/settings.html
    icon: bi bi-globe
tldri18n_status: 2
---
# settings

Récupère les informations du système d'exploitation Android.
Plus d'informations : <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Affiche une liste des paramètres de l'espace de nom `global` :

`settings list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global</span>

- Récupère la valeur d'un paramètre :

`settings get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">airplane_mode_on</span>

- Assigne une valeur à un paramètre :

`settings put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screen_brightness</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- Supprime un paramètre :

`settings delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secure</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screensaver_enabled</span>
