---
layout: page
title: android/input (中文 (繁體, 台灣))
description: "將事件代碼或觸控螢幕手勢傳送到 Android 裝置。"
content_hash: a350b50e0fa97a99591752954802bf9c9e2371d2
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
tldri18n_status: 2
---
# input

將事件代碼或觸控螢幕手勢傳送到 Android 裝置。
此命令只能透過 `adb shell` 使用。
更多資訊：<https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- 將單個字元的事件代碼傳送到 Android 裝置：

`input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">事件代碼</span>

- 將文字傳送到 Android 裝置（`%s` 代表空格）：

`input text "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文字</span>`"`

- 將輕觸發送到 Android 裝置：

`input tap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x 值</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y 值</span>

- 將滑動手勢傳送到 Android 裝置：

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x 開始值</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y 開始值</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x 結束值</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y 結束值</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">持續時間（微秒）</span>

- 使用滑動手勢將長按傳送到 Android 裝置：

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x 值</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y 值</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x 值</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y 值</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">持續時間（微秒）</span>
