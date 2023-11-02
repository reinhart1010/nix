---
layout: page
title: android/pm (বাংলা)
description: "একটি Android ডিভাইসে অ্যাপ্লিকেশন সম্পর্কে তথ্য দেখান।"
content_hash: 3abf2d447e63bc84a4e5e75da1905b4fe5329b38
last_modified_at: 2023-11-02
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
  - title: فارسی version
    url: /fa/android/pm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/pm.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/android/pm.html
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
  - title: українська version
    url: /uk/android/pm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/pm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/pm.html
    icon: bi bi-globe
---
# pm

একটি Android ডিভাইসে অ্যাপ্লিকেশন সম্পর্কে তথ্য দেখান।
আরও তথ্য পাবেন: <https://developer.android.com/studio/command-line/adb#pm>।

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
