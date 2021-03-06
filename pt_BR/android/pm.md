---
layout: page
title: android/pm (português (Brasil))
description: "Executa ações e consultas em pacotes de apps instalados no dispositivo."
content_hash: 5b5e0381d98d37876f4dafccd855a58fd7d8e1f5
related_topics:
  - title: Deutsch version
    url: /de/android/pm.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/pm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/pm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/pm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/pm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/pm.html
    icon: bi bi-globe
---
# pm

Executa ações e consultas em pacotes de apps instalados no dispositivo.
Mais informações: <https://developer.android.com/studio/command-line/adb#pm>.

- Exibe uma lista com todos os apps instalados:

`pm list packages`

- Exibe uma lista com todos os apps do sistema instalado:

`pm list packages -s`

- Exibe uma lista com todos os apps de terceiros instalados:

`pm list packages -3`

- Exibe uma lista com todos os apps cujos nomes estejam incluídos em palavras-chave:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavras_chave</span>

- Exibe o caminho para o APK de um app:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app</span>
