---
layout: page
title: common/alias (বাংলা)
description: "উপনাম তৈরি করে -- এই শব্দগুলি যেগুলি কমান্ড স্ট্রিং দ্বারা প্রতিস্থাপন করা হয়।"
content_hash: 01cbc6ebbe8864e81784c2418662fbb857dd5613
last_modified_at: 2023-11-06
related_topics:
  - title: Deutsch version
    url: /de/common/alias.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/alias.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alias.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/alias.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alias.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/alias.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/alias.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alias.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/alias.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alias.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/alias.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alias.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alias.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/alias.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/alias.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/alias.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/alias.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/alias.html
    icon: bi bi-globe
---
# alias

উপনাম তৈরি করে -- এই শব্দগুলি যেগুলি কমান্ড স্ট্রিং দ্বারা প্রতিস্থাপন করা হয়।
উপনাম বর্তমান শেল সেশনে শেষ হয় যতক্ষণ না সেট করা হয়, উদাহরণ: `~/.bashrc`।
আরও তথ্য পাবেন: <https://tldp.org/LDP/abs/html/aliases.html>।

- সমস্ত উপনামের তালিকা তৈরি করুন:

`alias`

- একটি সাধারণ উপনাম তৈরি করুন:

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">শব্দ</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">কমান্ড</span>`"`

- দেওয়া উপনামে সংক্ষিপ্ত কমান্ড দেখুন:

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">শব্দ</span>

- একটি উপনাম বাদ দিন:

`unalias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">শব্দ</span>

- `rm` কে একটি ইন্টারয়াক্টিভ কমান্ড হিসেবে পরিবর্তন করুন:

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rm</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rm --interactive</span>`"`

- `ls -a` এর সংক্ষেপ রূপ হিসেবে `la` তৈরি করুন:

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">la</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -all</span>`"`
