---
layout: page
title: windows/find (বাংলা)
description: "এক বা একাধিক ফাইলে নির্দিষ্ট স্ট্রিং খোঁজা।"
content_hash: d87dc7f3ac00ffe9a3fffc03fb6fbe6971867eb2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/find.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/find.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/find.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/find.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/find.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/find.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/find.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/find.html
    icon: bi bi-globe
tldri18n_status: 2
---
# find

এক বা একাধিক ফাইলে নির্দিষ্ট স্ট্রিং খোঁজা।
আরও তথ্য পাবেন: <https://learn.microsoft.com/windows-server/administration/windows-commands/find>।

- ঐ স্ট্রিং যুক্ত লাইন গুলি খোঁজা:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">স্ট্রিং</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পথ\হতে\ফাইল_বা_ডিরেক্টরি</span>

- সেই লাইন গুলি প্রদর্শন করুন যেগুলিতে নির্দিষ্ট স্ট্রিং নেই:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">স্ট্রিং</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পথ\হতে\ফাইল_বা_ডিরেক্টরি</span>` /v`

- নির্দিষ্ট স্ট্রিং সহ লাইন সংখ্যা দেখানো:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">স্ট্রিং</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পথ\হতে\ফাইল_বা_ডিরেক্টরি</span>` /c`

- লাইন সংখ্যা দিয়ে লাইন এর সাথে লাইন এর তালিকা দেখানো:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">স্ট্রিং</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পথ\হতে\ফাইল_বা_ডিরেক্টরি</span>` /n`
