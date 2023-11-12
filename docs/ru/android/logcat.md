---
layout: page
title: android/logcat (русский)
description: "Дамп лог (журнал) системных сообщений, включая трассировку стека при возникновении ошибки и информационные сообщения, регистрируемые приложениями."
content_hash: d2bf16ab760d6039d57f1a9e62a12af295dc9cf9
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
  - title: português (Portugal) version
    url: /pt_PT/android/logcat.html
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

Дамп лог (журнал) системных сообщений, включая трассировку стека при возникновении ошибки и информационные сообщения, регистрируемые приложениями.
Больше информации: <https://developer.android.com/studio/command-line/logcat>.

- Показать системные логи:

`logcat`

- Записать системные логи в файл:

`logcat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Показать строки, соответствующие регулярному выражению:

`logcat --regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">регулярное_выражение</span>
