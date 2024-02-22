---
layout: page
title: android/am (中文 (繁體, 台灣))
description: "Android 活動管理器。"
content_hash: c473719a9b899ad6d447295c36c01321b6373b99
last_modified_at: 2024-02-22
related_topics:
  - title: বাংলা version
    url: /bn/android/am.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/am.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/am.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/am.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/android/am.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/am.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/android/am.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/am.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/android/am.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/android/am.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/android/am.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/android/am.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/am.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/am.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/am.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/am.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/am.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/am.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/android/am.html
    icon: bi bi-globe
  - title: o‘zbek version
    url: /uz/android/am.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/am.html
    icon: bi bi-globe
tldri18n_status: 2
---
# am

Android 活動管理器。
更多資訊：<https://developer.android.com/tools/adb#am>.

- 啟動一個指定的活動：

`am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.android.settings/.Settings</span>

- 啟動一個活動並將資料傳遞給它：

`am start -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.action.VIEW</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tel:123</span>

- 啟動與特定操作和類別匹配的活動：

`am start -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.action.MAIN</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.category.HOME</span>

- 將意圖（intent）轉換為 URI：

`am to-uri -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.action.VIEW</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tel:123</span>
