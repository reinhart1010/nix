---
layout: page
title: android/input (Nederlands)
description: "Stuur gebeurteniscodes of touchscreen-gebaren naar een Android-apparaat."
content_hash: 108bc333f601ac3e9d4ea29b18280064585da5c0
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

Stuur gebeurteniscodes of touchscreen-gebaren naar een Android-apparaat.
Dit commando kan alleen worden gebruikt via `adb shell`.
Meer informatie: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Stuur een gebeurteniscode voor een enkel teken naar een Android-apparaat:

`input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">event_code</span>

- Stuur een tekst naar een Android-apparaat (`%s` vertegenwoordigt spaties):

`input text "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>`"`

- Stuur een enkele tik naar een Android-apparaat:

`input tap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_position</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_position</span>

- Stuur een swipe-gebaar naar een Android-apparaat:

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_start</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_start</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_end</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_end</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duration_in_ms</span>

- Stuur een lange druk naar een Android-apparaat met behulp van een swipe-gebaar:

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_position</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_position</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_position</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_position</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duration_in_ms</span>
