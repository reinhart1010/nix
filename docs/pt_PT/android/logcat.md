---
layout: page
title: android/logcat (português (Portugal))
description: "Exibe um conjunto de mensagens de sistema, incluindo a stack de execução do programa em caso de erro, e mensagens de informação criadas por aplicações."
content_hash: e8b204fdfd5da58232643d4a77a84d023938be60
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/android/logcat.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/logcat.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/logcat.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/logcat.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/android/logcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/logcat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/android/logcat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/logcat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/android/logcat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/android/logcat.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/logcat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/logcat.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/logcat.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/logcat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/logcat.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/android/logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/logcat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/logcat.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># logcat

Exibe um conjunto de mensagens de sistema, incluindo a stack de execução do programa em caso de erro, e mensagens de informação criadas por aplicações.
Mais informações: <https://developer.android.com/studio/command-line/logcat>.

- Mostrar mensagens de sistema:

`logcat`

- Escrever as mensagens de sistema num ficheiro:

`logcat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Mostrar mensagens que correspondem a uma expressão regular:

`logcat --regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressao_regular</span>
