---
layout: page
title: android/pm (中文 (繁體, 台灣))
description: "顯示關於 Android 裝置上的應用程式的資訊。"
content_hash: f4726e72ca52f673d1c13a2a98bcb7ba35dc9592
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
  - title: português (Brasil) version
    url: /pt_BR/android/pm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/pm.html
    icon: bi bi-globe
---
# pm

顯示關於 Android 裝置上的應用程式的資訊。
更多資訊：<https://developer.android.com/studio/command-line/adb#pm>.

- 印出所有已安裝應用程式的列表：

`pm list packages`

- 印出所有已安裝的系統應用程式的列表：

`pm list packages -s`

- 印出所有已安裝的第三方應用程式的列表：

`pm list packages -3`

- 印出與指定關鍵字匹配的應用程式列表：

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">關鍵詞</span>

- 印出指定應用程式的 APK 的路徑：

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">應用名</span>
