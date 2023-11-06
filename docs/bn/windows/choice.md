---
layout: page
title: windows/choice (বাংলা)
description: "ব্যবহারকারীকে একটি চয়েস নির্বাচন করতে উৎসাহিত করুন এবং নির্বাচিত চয়েস ইনডেক্স ফিরিয়ে দিন।"
content_hash: 5381a954ddd1a28bf7c921cf0847afa3d96ee027
last_modified_at: 2023-11-06
related_topics:
  - title: English version
    url: /en/windows/choice.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choice.html
    icon: bi bi-globe
---
# choice

ব্যবহারকারীকে একটি চয়েস নির্বাচন করতে উৎসাহিত করুন এবং নির্বাচিত চয়েস ইনডেক্স ফিরিয়ে দিন।
আরও তথ্য পাবেন: <https://learn.microsoft.com/windows-server/administration/windows-commands/choice>।

- বর্তমান ব্যবহারকারীকে `Y` বা `N` চয়েস নির্বাচন করতে:

`choice`

- বর্তমান ব্যবহারকারীকে একটি নির্দিষ্ট সেট থেকে [c]hoice নির্বাচন করতে:

`choice /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AB</span>

- বর্তমান ব্যবহারকারীকে একটি চয়েস নির্বাচন করতে একটি নির্দিষ্ট [m]essage সহ:

`choice /m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">বার্তা</span>`"`

- বর্তমান ব্যবহারকারীকে একটি [c]ase-[s]ensitive [c]hoice নির্বাচন করতে একটি নির্দিষ্ট সেট থেকে:

`choice /cs /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Ab</span>

- বর্তমান ব্যবহারকারীকে একটি চয়েস নির্বাচন করতে এবং একটি নির্দিষ্ট [t]ime এ [d]efault চয়েস এ প্রাথমিকভাবে পছন্দ করতে:

`choice /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- সাহায্য দেখান:

`choice /?`
