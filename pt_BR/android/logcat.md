---
layout: page
title: android/logcat (português (Brasil))
description: "Despeja um registro de mensagens do sistema."
content_hash: c94e0f22d2c19134d6cf79268677aa583793649f
related_topics:
  - title: Deutsch version
    url: /de/android/logcat.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/logcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/logcat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/logcat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/logcat.html
    icon: bi bi-globe
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
