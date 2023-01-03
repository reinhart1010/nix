---
layout: page
title: android/dumpsys (বাংলা)
description: "অ্যান্ড্রয়েড সিস্টেম পরিষেবা সম্পর্কে তথ্য প্রদান করে।"
content_hash: f9828256bb273d39d405b304414795dca5096624
last_modified_at: 2023-01-03
related_topics:
  - title: Deutsch version
    url: /de/android/dumpsys.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/dumpsys.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/dumpsys.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/dumpsys.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/dumpsys.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/dumpsys.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/dumpsys.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/dumpsys.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/dumpsys.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/dumpsys.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/dumpsys.html
    icon: bi bi-globe
  - title: o‘zbek version
    url: /uz/android/dumpsys.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/dumpsys.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/dumpsys.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dumpsys

অ্যান্ড্রয়েড সিস্টেম পরিষেবা সম্পর্কে তথ্য প্রদান করে।
এই কমান্ডটি শুধুমাত্র `adb shell` এর মাধ্যমে ব্যবহার করা যেতে পারে।
আরও তথ্য পাবেন: <https://developer.android.com/studio/command-line/dumpsys>.

- সমস্ত সিস্টেম পরিষেবার জন্য ডায়াগনস্টিক আউটপুট পান:

`dumpsys`

- একটি নির্দিষ্ট সিস্টেম পরিষেবার জন্য ডায়গনিস্টিক আউটপুট পান:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পরিষেবা</span>

- 'ডাম্পসিস' যে সমস্ত পরিষেবা সম্পর্কে তথ্য দিতে পারে তাদের তালিকা করুন:

`dumpsys -l`

- একটি পরিষেবার জন্য পরিষেবা-নির্দিষ্ট আর্গুমেন্ট তালিকা করুন:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পরিষেবা</span>` -h`

- ডায়গনিস্টিক আউটপুট থেকে একটি নির্দিষ্ট পরিষেবা বাদ দিন:

`dumpsys -- skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পরিষেবা</span>

- সেকেন্ডে একটি সময়সীমা নির্দিষ্ট করুন (ডিফল্ট 10 সেকেন্ড):

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..অসীম</span>
