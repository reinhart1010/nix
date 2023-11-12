---
layout: page
title: android/input (русский)
description: "Отправить коды событий или жесты сенсорного экрана на устройство Android."
content_hash: 5b5027f18d954c68054dd31979d8d033354e75e4
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
  - title: italiano version
    url: /it/android/input.html
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

Отправить коды событий или жесты сенсорного экрана на устройство Android.
Эту команду можно использовать только через `adb shell`.
Больше информации: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Отправить код события для одного символа на устройство Android:

`input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">код_события</span>

- Отправить текст на устройство Android (`%s` означает пробел):

`input text "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">текст</span>`"`

- Отправить одно нажатие на экран на устройство Android:

`input tap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">х_позиция</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_позиция</span>

- Отправить жест смахивания на устройство Android:

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_начало</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_начало</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_конец</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_конец</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">продолжительность_в_мс</span>

- Отправить длинное нажатие на экран на устройство Android с помощью жеста смахивания:

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_position</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_position</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_position</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_pos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">продолжительность_в_мс</span>
