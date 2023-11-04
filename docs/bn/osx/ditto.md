---
layout: page
title: osx/ditto (বাংলা)
description: "ফাইল এবং ডিরেক্টরি কপি করুন।"
content_hash: 0f3a078fc9f95c8ba63f41339ea26e3ed6784df8
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/osx/ditto.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/ditto.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/ditto.html
    icon: bi bi-globe
---
# ditto

ফাইল এবং ডিরেক্টরি কপি করুন।
আরও তথ্য পাবেন: <https://ss64.com/osx/ditto.html>.

- সোর্স ডিরেক্টরির বিষয়বস্তু দিয়ে  গন্তব্য ডিরেক্টরির বিষয়বস্তু ওভাররাইট করুন:

`ditto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">সোর্স/এর/পথ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">গন্তব্য/এর/পথ</span>

- কপি করা প্রতিটি ফাইলের জন্য টার্মিনাল উইন্ডোতে একটি লাইন প্রিন্ট করুন:

`ditto -V `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">সোর্স/এর/পথ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">গন্তব্য/এর/পথ</span>

- মূল ফাইল এর পারমিশন বজায় রেখে একটি প্রদত্ত ফাইল বা ডিরেক্টরি কপি করুন:

`ditto -rsrc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">সোর্স/এর/পথ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">গন্তব্য/এর/পথ</span>
