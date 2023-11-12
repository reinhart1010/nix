---
layout: page
title: android/logcat (português (Brasil))
description: "Despeja um registro de mensagens do sistema."
content_hash: 829689fe3b0cb8b2495b9a1466faa8994af685cc
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
  - title: português (Portugal) version
    url: /pt_PT/android/logcat.html
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
tldri18n_status: 2
---
# logcat

Despeja um registro de mensagens do sistema.
Mais informações: <https://developer.android.com/studio/command-line/logcat>.

- Exibe a saída do registro:

`logcat`

- Salva a saída da mensagem de registro em um arquivo:

`logcat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Exibe apenas linhas em que a mensagem de registro corresponda a uma expressão regular:

`logcat --regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressao_regular</span>

- Exibe logs para um PID específico:

`logcat --pid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Exibe logs de processo de um pacote específico:

`logcat --pid=$(pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>`)`
