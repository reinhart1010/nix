---
layout: page
title: osx/ditto (বাংলা)
description: "ফাইল এবং ডিরেক্টরি কপি করুন।"
content_hash: 2cb0c36a7f606c4b1e15aa8278001d3188a242d6
last_modified_at: 2024-01-31
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
tldri18n_status: 2
---
# ditto

ফাইল এবং ডিরেক্টরি কপি করুন।
আরও তথ্য পাবেন: <https://keith.github.io/xcode-man-pages/ditto.1.html>।

- সোর্স ডিরেক্টরির বিষয়বস্তু দিয়ে  গন্তব্য ডিরেক্টরির বিষয়বস্তু ওভাররাইট করুন:

`ditto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">সোর্স/এর/পথ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">গন্তব্য/এর/পথ</span>

- কপি করা প্রতিটি ফাইলের জন্য টার্মিনাল উইন্ডোতে একটি লাইন প্রিন্ট করুন:

`ditto -V `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">সোর্স/এর/পথ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">গন্তব্য/এর/পথ</span>

- মূল ফাইল এর পারমিশন বজায় রেখে একটি প্রদত্ত ফাইল বা ডিরেক্টরি কপি করুন:

`ditto -rsrc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">সোর্স/এর/পথ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">গন্তব্য/এর/পথ</span>
