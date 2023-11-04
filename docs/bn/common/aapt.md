---
layout: page
title: common/aapt (বাংলা)
description: "এন্ড্রয়েড এসেট প্যাকেজিং টুল।"
content_hash: ed65048f750e0dae25a2b714535ffdc9b5a8a7a8
last_modified_at: 2023-11-04
related_topics:
  - title: Deutsch version
    url: /de/common/aapt.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aapt.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aapt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aapt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/aapt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aapt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aapt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/aapt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aapt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/aapt.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aapt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aapt.html
    icon: bi bi-globe
---
# aapt

এন্ড্রয়েড এসেট প্যাকেজিং টুল।
এন্ড্রয়েড অ্যাপের সম্পদগুলি সংকলিত এবং প্যাকেজ করুন।
আরও জানতে: <https://elinux.org/Android_aapt>.

- APK সংগ্রহে অন্তর্ভুক্ত ফাইলের তালিকা তৈরি করুন:

`aapt list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">অ্যাপ.apk/এর/পথ</span>

- একটি অ্যাপের মেটাডেটা (সংস্করণ, অনুমতি, ইত্যাদি) দেখানোর জন্য:

`aapt dump badging `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">অ্যাপ.apk/এর/পথ</span>

- নির্দিষ্ট ডিরেক্টরি সহ ফাইলগুলির সাথে একটি নতুন APK সংগ্রহ তৈরি করুন:

`aapt package -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">অ্যাপ.apk/এর/পথ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ডিরেক্টরি/এর/পথ</span>
