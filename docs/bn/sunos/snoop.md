---
layout: page
title: sunos/snoop (বাংলা)
description: "নেটওয়ার্ক প্যাকেট স্নিফার।"
content_hash: c8125bf2c29dc895dc6d5aac0c2bc1483327124a
last_modified_at: 2023-11-06
related_topics:
  - title: English version
    url: /en/sunos/snoop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/snoop.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/snoop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/snoop.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/snoop.html
    icon: bi bi-globe
---
# snoop

নেটওয়ার্ক প্যাকেট স্নিফার।
SunOS এর জন্য tcpdump এর সমতুল্য।
আরও তথ্য পাবেন: <https://www.unix.com/man-page/sunos/1m/snoop>।

- একটি নির্দিষ্ট নেটওয়ার্ক ইন্টারফেসে প্যাকেটগুলি ক্যাপচার করুন:

`snoop -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">e1000g0</span>

- ক্যাপচার করা প্যাকেটগুলিকে প্রদর্শন করার পরিবর্তে একটি ফাইলে সংরক্ষণ করুন:

`snoop -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইলের_নাম</span>

- একটি ফাইল থেকে প্যাকেটের ভার্বোজ প্রোটোকল লেয়ারের সারাংশ প্রদর্শন করুন:

`snoop -V -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইলের_নাম</span>

- একটি হোস্টনাম থেকে আসা নেটওয়ার্ক প্যাকেটগুলি ক্যাপচার করুন এবং একটি প্রদত্ত পোর্টে যান:

`snoop to port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পোর্ট</span>` from host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">হোস্টনাম</span>

- দুটি আইপি ঠিকানার মধ্যে বিনিময় করা নেটওয়ার্ক প্যাকেটের একটি হেক্স-ডাম্প ক্যাপচার করুন এবং প্রদর্শন করুন:

`snoop -x0 -p4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">আইপি_ঠিকানা_১</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">আইপি_ঠিকানা_২</span>
