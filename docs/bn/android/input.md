---
layout: page
title: android/input (বাংলা)
description: "একটি Android ডিভাইসে ইভেন্ট কোড বা টাচস্ক্রিন অঙ্গভঙ্গি পাঠান।"
content_hash: bdd0fb771468526516b72a82a359da340882cf06
last_modified_at: 2023-01-03
related_topics:
  - title: Deutsch version
    url: /de/android/input.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/input.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/input.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/input.html
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
  - title: 中文 version
    url: /zh/android/input.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/input.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># input

একটি Android ডিভাইসে ইভেন্ট কোড বা টাচস্ক্রিন অঙ্গভঙ্গি পাঠান।
এই কমান্ডটি শুধুমাত্র `adb shell` এর মাধ্যমে ব্যবহার করা যেতে পারে।
আরও তথ্য পাবেন: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- একটি Android ডিভাইসে একটি একক অক্ষরের জন্য একটি ইভেন্ট কোড পাঠান:

`input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ইভেন্ট_কোড</span>

- একটি অ্যান্ড্রয়েড ডিভাইসে একটি পাঠ্য পাঠান (`%s` স্পেস প্রতিনিধিত্ব করে):

`input text "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">স্ট্রিং</span>`"`

- একটি Android ডিভাইসে একটি একক ট্যাপ পাঠান:

`input tap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_অবস্থান</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_অবস্থান</span>

- একটি Android ডিভাইসে একটি সোয়াইপ অঙ্গভঙ্গি পাঠান:

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_শুরু</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_শুরু</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_শেষ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_শেষ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..অসীম</span>

- একটি সোয়াইপ অঙ্গভঙ্গি ব্যবহার করে একটি Android ডিভাইসে একটি দীর্ঘ প্রেস পাঠান:

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_অবস্থান</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_অবস্থান</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_অবস্থান</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_অবস্থান</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..অসীম</span>
