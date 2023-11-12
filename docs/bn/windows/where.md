---
layout: page
title: windows/where (বাংলা)
description: "অনুসন্ধান প্যাটার্নের সাথে মিলছে ফাইলগুলির অবস্থান প্রদর্শন করুন।"
content_hash: 7674160efe3ee321a96b7356f3a678ef32549e71
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/where.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/windows/where.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/where.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/where.html
    icon: bi bi-globe
tldri18n_status: 2
---
# where

অনুসন্ধান প্যাটার্নের সাথে মিলছে ফাইলগুলির অবস্থান প্রদর্শন করুন।
ডিফল্টস্ কারেন্ট ওয়ার্ক ডিরেক্টরি এবং PATH এনভায়রনমেন্ট ভেরিয়েবলে পাথের অবস্থানগুলি।
আরও তথ্য পাবেন: <https://learn.microsoft.com/windows-server/administration/windows-commands/where>।

- ফাইল প্যাটার্নের অবস্থান প্রদর্শন করুন:

`where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইল_প্যাটার্ন</span>

- ফাইল প্যাটার্নের অবস্থান প্রদর্শন করুন যাতে ফাইলের আকার এবং তারিখও থাকে:

`where /T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইল_প্যাটার্ন</span>

- নির্দিষ্ট পথে ফাইল প্যাটার্নের জন্য পুনরাবৃত্তি অনুসন্ধান করুন:

`where /R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পথ\টু\ডিরেক্টরি</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইল_প্যাটার্ন</span>

- ফাইল প্যাটার্নের অবস্থানের জন্য শান্তভাবে ত্রুটি কোড ফিরিয়ে আসুন:

`where /Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইল_প্যাটার্ন</span>
