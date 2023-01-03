---
layout: page
title: android/pm (বাংলা)
description: "একটি Android ডিভাইসে অ্যাপ্লিকেশন সম্পর্কে তথ্য দেখান।"
content_hash: 180f0b49a1f6c756e5efa1e194631936e3e866b1
last_modified_at: 2023-01-03
related_topics:
  - title: Deutsch version
    url: /de/android/pm.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/pm.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/pm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/pm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/pm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/pm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/pm.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/pm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/pm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/pm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/pm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/pm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/pm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pm

একটি Android ডিভাইসে অ্যাপ্লিকেশন সম্পর্কে তথ্য দেখান।
আরও তথ্য পাবেন: <https://developer.android.com/studio/command-line/adb#pm>.

- সমস্ত ইনস্টল করা অ্যাপের একটি তালিকা প্রিন্ট করুন:

`pm list packages`

- সমস্ত ইনস্টল করা সিস্টেম অ্যাপের একটি তালিকা প্রিন্ট করুন:

`pm list packages -s`

- সমস্ত ইনস্টল করা থার্ড-পার্টি অ্যাপের একটি তালিকা প্রিন্ট করুন:

`pm list packages -3`

- নির্দিষ্ট কীওয়ার্ডের সাথে মিলে যাওয়া অ্যাপগুলির একটি তালিকা প্রিন্ট করুন:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">কীওয়ার্ড১ কীওয়ার্ড২...</span>

- একটি নির্দিষ্ট অ্যাপের APK এর পথ প্রিন্ট করুন:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">অ্যাপ</span>
