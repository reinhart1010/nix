---
layout: page
title: android/input (italiano)
description: "Invia codici evento o gesture touchscreen a un dispositivo Android."
content_hash: 85a57866bb8db9d28b1c192f960eb1700a82e4c5
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/android/input.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/input.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/input.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/input.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/android/input.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/input.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/android/input.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/input.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/android/input.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/input.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/input.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/input.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/input.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/input.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/input.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/android/input.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/input.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/input.html
    icon: bi bi-globe
tldri18n_status: 2
---
# input

Invia codici evento o gesture touchscreen a un dispositivo Android.
Questo comando può essere usato solo attraverso `abd shell`.
Maggiori informazioni: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Invia un codice evento per un singolo carattere a un dispositivo Android:

`input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codice_evento</span>

- Invia un testo a un dispositivo Android (`%s` rappresenta lo spazio):

`input text "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testo</span>`"`

- Invia un singolo tap a un dispositivo Android:

`input tap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pos_x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pos_y</span>

- Invia una gesture di scorrimento a un dispositivo Android:

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inizio_x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inizio_y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fine_x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fine_y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">durata_in_ms</span>

- Invia un tap lungo a un dispositivo Android usando una gesture di scorrimento:

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pos_x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pos_y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pos_x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pos_y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">durata_in_ms</span>
