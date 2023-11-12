---
layout: page
title: android/input (português (Brasil))
description: "Envia códigos de evento ou gestos de toque para um dispositivo Android."
content_hash: cc155e8bee606aec5484c6fee9ea0257bdb9a335
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

Envia códigos de evento ou gestos de toque para um dispositivo Android.
Esse comando só pode ser usado através de `adb shell`.
Mais informações: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Envia um código de evento de um caractere para um dispositivo Android:

`input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codigo_de_evento</span>

- Envia texto para um dispositivo Android (`%s` representa espaços):

`input text "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto</span>`"`

- Envia um único toque para um dispositivo Android:

`input tap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_pos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_pos</span>

- Envia um gesto de deslizar para um dispositivo Android:

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_inicio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_inicio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_fim</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_fim</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duração_em_ms</span>

- Envia um pressionamento longo usando gesto de deslizar para um dispositivo Android:

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_pos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_pos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_pos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_pos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duração_em_ms</span>
