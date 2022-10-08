---
layout: page
title: android/logcat (italiano)
description: "Scarica il registro dei messaggi di sistema, comprese le stack traces quando si verifica un errore, e i messaggi di log delle applicazioni."
content_hash: 9f1c58ce60912cd2162f2f9bb418e57002be9c62
related_topics:
  - title: Deutsch version
    url: /de/android/logcat.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/logcat.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/logcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/logcat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/logcat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/logcat.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/logcat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/logcat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/logcat.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># logcat

Scarica il registro dei messaggi di sistema, comprese le stack traces quando si verifica un errore, e i messaggi di log delle applicazioni.
Maggiori informazioni: <https://developer.android.com/studio/command-line/logcat>.

- Mostra il log di sistema:

`logcat`

- Scrivi il log di sistema su file:

`logcat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>

- Mostra le righe corrispondenti ad una specifica espressione regolare:

`logcat --regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">espressione_regolare</span>
