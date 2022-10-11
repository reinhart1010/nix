---
layout: page
title: android/cmd (português (Portugal))
description: "Gestor de serviços (service manager) do Android."
content_hash: 99dbdebcd7e1a27f959df318cca25ebdf4ccb9f3
related_topics:
  - title: বাংলা version
    url: /bn/android/cmd.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/cmd.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/cmd.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/cmd.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/cmd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/android/cmd.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/cmd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/cmd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/cmd.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/cmd.html
    icon: bi bi-globe
  - title: o‘zbek version
    url: /uz/android/cmd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/cmd.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/cmd.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cmd

Gestor de serviços (service manager) do Android.
Mais informações: <https://cs.android.com/android/platform/superproject/+/master:frameworks/native/cmds/cmd/>.

- Listar todos os serviços em execução:

`cmd -l`

- Executar um serviço específico:

`cmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alarm</span>

- Executar um serviço com parâmetros:

`cmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vibrator</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vibrate 300</span>
