---
layout: page
title: android/logcat (français)
description: "Exporte une log depuis les messages système."
content_hash: 858bedc81e61fbe1f0b91eab1c9bfd35a235837f
related_topics:
  - title: Deutsch version
    url: /de/android/logcat.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/logcat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/logcat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/logcat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/logcat.html
    icon: bi bi-globe
---
# logcat

Exporte une log depuis les messages système.
Plus d'informations : <https://developer.android.com/studio/command-line/logcat>.

- Affiche la journalisation système :

`logcat`

- Écris la journalisation système dans un fichier :

`logcat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Affiche les lignes qui correspondent à une expression régulière :

`logcat --regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_régulière</span>
