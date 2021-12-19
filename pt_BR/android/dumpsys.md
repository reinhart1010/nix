---
layout: page
title: android/dumpsys (português (Brasil))
description: "Fornece informações sobre os serviços do sistema Android."
content_hash: 6297006a44d8b8eb9c956f69b89036985398b873
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

Fornece informações sobre os serviços do sistema Android.
Este comando só pode ser usado através de `adb shell`.
Mais informações: <https://developer.android.com/studio/command-line/dumpsys>.

- Gera um diagnóstico de todos os serviços do sistema:

`dumpsys`

- Gera um diagnóstico de um serviço do sistema específico:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servico</span>

- Lista todos os serviços que o `dumpsys` pode obter informações:

`dumpsys -l`

- Lista argumentos específicos-de-um-serviço para um serviço:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servico</span>` -h`

- Omite um serviço em específico do diagnóstico:

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servico</span>

- Específica um periodo de _timeout_ (por padrão é 10s):

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segundos</span>
