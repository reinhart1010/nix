---
layout: page
title: android/logcat (বাংলা)
description: "সিস্টেম বার্তার একটি লগ ডাম্প করুন, যখন একটি ত্রুটি ঘটেছে স্ট্যাক ট্রেস সহ, এবং অ্যাপ্লিকেশন দ্বারা লগ করা তথ্য বার্তা।"
content_hash: 987020b5c67963e4b1ecce3c4579531a9c168e35
last_modified_at: 2023-11-06
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
  - title: українська version
    url: /uk/android/logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/logcat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/logcat.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/android/logcat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># logcat

সিস্টেম বার্তার একটি লগ ডাম্প করুন, যখন একটি ত্রুটি ঘটেছে স্ট্যাক ট্রেস সহ, এবং অ্যাপ্লিকেশন দ্বারা লগ করা তথ্য বার্তা।
আরও তথ্য পাবেন: <https://developer.android.com/studio/command-line/logcat>।

- সিস্টেম লগগুলি প্রদর্শন করুন:

`logcat`

- একটি ফাইলে সিস্টেম লগ লিখুন:

`logcat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইলের/পথ</span>

- রেগুলার এক্সপ্রেশনের সাথে মেলে এমন লাইনগুলি প্রদর্শন করুন:

`logcat --regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">সাধারণ_অভিব্যক্তি</span>
