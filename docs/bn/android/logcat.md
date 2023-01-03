---
layout: page
title: android/logcat (বাংলা)
description: "সিস্টেম বার্তার একটি লগ ডাম্প করুন, যখন একটি ত্রুটি ঘটেছে স্ট্যাক ট্রেস সহ, এবং অ্যাপ্লিকেশন দ্বারা লগ করা তথ্য বার্তা।"
content_hash: 95c21118b508b16fd6fab6d12389758e028c76b2
last_modified_at: 2023-01-03
related_topics:
  - title: Deutsch version
    url: /de/android/logcat.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/logcat.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/logcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/logcat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/logcat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/android/logcat.html
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># logcat

সিস্টেম বার্তার একটি লগ ডাম্প করুন, যখন একটি ত্রুটি ঘটেছে স্ট্যাক ট্রেস সহ, এবং অ্যাপ্লিকেশন দ্বারা লগ করা তথ্য বার্তা।
আরও তথ্য পাবেন: <https://developer.android.com/studio/command-line/logcat>.

- সিস্টেম লগগুলি প্রদর্শন করুন:

`logcat`

- একটি ফাইলে সিস্টেম লগ লিখুন:

`logcat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইলের/পথ</span>

- রেগুলার এক্সপ্রেশনের সাথে মেলে এমন লাইনগুলি প্রদর্শন করুন:

`logcat --regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">সাধারণ_অভিব্যক্তি</span>
