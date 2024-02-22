---
layout: page
title: android/am (português (Portugal))
description: "Gestor de atividades do Android (Activity Manager)."
content_hash: 02d13cdfa357d796e9c8d26bcc8864a1450a30f2
last_modified_at: 2024-02-22
related_topics:
  - title: বাংলা version
    url: /bn/android/am.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/am.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/am.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/am.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/android/am.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/am.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/android/am.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/am.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/android/am.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/android/am.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/android/am.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/android/am.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/am.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/am.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/am.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/am.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/am.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/android/am.html
    icon: bi bi-globe
  - title: o‘zbek version
    url: /uz/android/am.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/am.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/am.html
    icon: bi bi-globe
tldri18n_status: 2
---
# am

Gestor de atividades do Android (Activity Manager).
Mais informações: <https://developer.android.com/tools/adb#am>.

- Inicia uma atividade específica:

`am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.android.settings/.Settings</span>

- Inicia uma atividade e passar-lhe dados:

`am start -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.action.VIEW</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tel:123</span>

- Inicia uma atividade com uma ação e categoria específicas:

`am start -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.action.MAIN</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.category.HOME</span>

- Converte um `intent` num URI:

`am to-uri -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.action.VIEW</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tel:123</span>
