---
layout: page
title: android/logcat (українська)
description: "Дамп журналу системних повідомлень, включаючи стек викликів, коли трапилась помилка, і інформаційні повідомлення, залоговані застосунками."
content_hash: ad55708a4aa47e89ac49bde546ab30bf4d92bed7
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
  - title: русский version
    url: /ru/android/logcat.html
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
tldri18n_status: 2
---
# logcat

Дамп журналу системних повідомлень, включаючи стек викликів, коли трапилась помилка, і інформаційні повідомлення, залоговані застосунками.
Більше інформації: <https://developer.android.com/studio/command-line/logcat>.

- Вивести системні логи:

`logcat`

- Записати системні логи в файл:

`logcat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Вивести рядки, які підпадають під регулярний вираз:

`logcat --regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">регулярний_вираз</span>

- Вивести логи для специфічного процесу (PID):

`logcat --pid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Вивести логи для процесу специфічного пакету:

`logcat --pid=$(pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>`)`
