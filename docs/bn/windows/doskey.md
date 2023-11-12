---
layout: page
title: windows/doskey (বাংলা)
description: "ম্যাক্রোজ, উইন্ডোজ কমান্ড এবং কমান্ড-লাইন পরিচালনা করুন।"
content_hash: cae9f8d0dfcdd2f6a67f125bdb55474eb13cd715
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/doskey.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/doskey.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/doskey.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/doskey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doskey

ম্যাক্রোজ, উইন্ডোজ কমান্ড এবং কমান্ড-লাইন পরিচালনা করুন।
আরও তথ্য পাবেন: <https://learn.microsoft.com/windows-server/administration/windows-commands/doskey>।

- উপস্থিত ম্যাক্রোগুলির তালিকা তৈরি করুন:

`doskey /macros`

- একটি নতুন ম্যাক্রো তৈরি করুন:

`doskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">নাম</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">কমান্ড</span>`"`

- একটি নির্দিষ্ট সম্পাদনযোগ্য জন্য একটি নতুন ম্যাক্রো তৈরি করুন:

`doskey /exename=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">সম্পাদন</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">নাম</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">কমান্ড</span>`"`

- ম্যাক্রো অপসারণ করুন:

`doskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">নাম</span>` =`

- মেমোরিতে সংরক্ষিত সমস্ত কমান্ড দেখান:

`doskey /history`

- পোর্টেবিলিটির জন্য ম্যাক্রোগুলি ফাইলে সংরক্ষণ করুন:

`doskey /macros > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইলের\পথ</span>

- একটি ফাইল থেকে ম্যাক্রোগুলি লোড করুন:

`doskey /macrofile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইলের\পথ</span>
