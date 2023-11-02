---
layout: page
title: windows/path (বাংলা)
description: "কার্যকর ফাইলগুলির জন্য পথ খোঁজা বা সেট করতে পারেন।"
content_hash: ed41f07d3b6e651d980bc3c9068d974236fba355
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/windows/path.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/path.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/path.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/path.html
    icon: bi bi-globe
---
# path

কার্যকর ফাইলগুলির জন্য পথ খোঁজা বা সেট করতে পারেন।
আরও তথ্য পাবেন: <https://learn.microsoft.com/windows-server/administration/windows-commands/path>।

- বর্তমান পথটি দেখানো:

`path`

- এক বা একাধিক নির্দিষ্ট ডিরেক্টরির জন্য পথ সেট করা:

`path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পথ\থেকে\ডিরেক্টরি1 পথ\থেকে\ডিরেক্টরি2 ...</span>

- মৌলিক পথে একটি নতুন ডিরেক্টরি যোগ করুন:

`path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পথ\থেকে\ডিরেক্টরি</span>`;%path%`

- কার্যকর ফাইলগুলির জন্য কেবলমাত্র বর্তমান ডিরেক্টরি খুঁজতে কমান্ড প্রম্প্ট সেট করুন:

`path ;`
