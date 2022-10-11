---
layout: page
title: android/dumpsys (português (Portugal))
description: "Fornece informações sobre os serviços do sistema Android."
content_hash: 98f3a027820aeb49f7f50033879ad199de669135
related_topics:
  - title: Deutsch version
    url: /de/android/dumpsys.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/dumpsys.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/dumpsys.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/dumpsys.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/dumpsys.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/dumpsys.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/dumpsys.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/dumpsys.html
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

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dumpsys

Fornece informações sobre os serviços do sistema Android.
Este comando só pode ser usado com a `adb shell`.
Mais informações: <https://developer.android.com/studio/command-line/dumpsys>.

- Gerar um diagnóstico de todos os serviços do sistema:

`dumpsys`

- Gerar um diagnóstico de um serviço do sistema específico:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servico</span>

- Listar todos os serviços dos quais o `dumpsys` pode obter informações:

`dumpsys -l`

- Listar argumentos específicos de um serviço para um serviço:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servico</span>` -h`

- Omitir um serviço em específico do diagnóstico:

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servico</span>

- Especificar um periodo de _timeout_ (por padrão é 10s):

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segundos</span>
