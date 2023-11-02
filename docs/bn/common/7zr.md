---
layout: page
title: common/7zr (বাংলা)
description: "একটি উচ্চ সঙ্কোচন অনুবাদক সাথে ফাইল অ্যার্কাইভার।"
content_hash: 4d226c7b3117c19c3b3e4352941301465ec76d3a
last_modified_at: 2023-11-02
related_topics:
  - title: Deutsch version
    url: /de/common/7zr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/7zr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/7zr.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/7zr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/7zr.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/7zr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/7zr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/7zr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/7zr.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/7zr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/7zr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/7zr.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/7zr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/7zr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/7zr.html
    icon: bi bi-globe
---
# 7zr

একটি উচ্চ সঙ্কোচন অনুবাদক সাথে ফাইল অ্যার্কাইভার।
`7z` এর মত, কিন্তু এটি কেবলমাত্র `.7z` ফাইলগুলি সমর্থন করে।
আরও তথ্য পেতে: <https://manned.org/7zr>|

- একটি ফাইল বা ডিরেক্টরি অ্যার্কাইভ করুন:

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/আর্কাইভ.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/ফাইল_অথবা_ডিরেক্টরি</span>

- একটি বিদ্যমান আর্কাইভ এনক্রিপ্ট করুন (ফাইলের নামগুলি সহ):

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/এনক্রিপ্টেড.7z</span>` -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাসওয়ার্ড</span>` -mhe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/আর্কাইভ.7z</span>

- একটি আর্কাইভ বিন্দুবর্তন রক্ষা করে একটি আর্কাইভ নেওয়া:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/আর্কাইভ.7z</span>

- একটি আর্কাইভটি একটি নির্দিষ্ট ডিরেক্টরিতে নেওয়া:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/আর্কাইভ.7z</span>` -o`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/আউটপুট</span>

- একটি আর্কাইভটি একটি `stdout` এ নেওয়া:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/আর্কাইভ.7z</span>` -so`

- একটি আর্কাইভের সামগ্রী তালিকা দেখুন:

`7zr l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/আর্কাইভ.7z</span>

- উপলব্ধ আর্কাইভ ধরণের তালিকা:

`7zr i`
