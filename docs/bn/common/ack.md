---
layout: page
title: common/ack (বাংলা)
description: "একটি গ্রেপের মত খোঁজ টুল, ডেভেলপারদের জন্য অপটিমাইজড করা."
content_hash: 05fdfde1f44235e5e1906dd25402f8b739d82048
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ack.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ack.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ack.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ack.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
---
# ack

একটি গ্রেপের মত খোঁজ টুল, ডেভেলপারদের জন্য অপটিমাইজড করা.
আরও দেখুন: `rg`, যা অধিক দ্রুত।
আরও তথ্য পেতে: <https://beyondgrep.com/documentation>.

- বর্তমান ডিরেক্টরির অব্যাপ্তিতে স্ট্রিং বা নিয়মিত অভিব্যক্তি সম্মিলিত ফাইলগুলি জন্য খোঁজ করুন:

`ack "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">খোঁজের_প্যাটার্ন</span>`"`

- একটি কেস-ইনসেনসিটিভ প্যাটার্ন খোঁজ করুন:

`ack --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">খোঁজের_প্যাটার্ন</span>`"`

- একটি প্যাটার্ন মেলে সার্থকভাবে খোঁজুন, [ও]ণলি ম্যাচ টেক্সট দেখানো না:

`ack -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">খোঁজের_প্যাটার্ন</span>`"`

- নির্দিষ্ট প্রকারের ফাইলগুলিতে সীমাবদ্ধ খোঁজ করুন:

`ack --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">খোঁজের_প্যাটার্ন</span>`"`

- নির্দিষ্ট প্রকারের ফাইলগুলিতে খোঁজুন না:

`ack --type=no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">খোঁজের_প্যাটার্ন</span>`"`

- পাওয়া মিলে সম্পূর্ণ ম্যাচের সম্পূর্ণ সংখ্যা গণনা করুন:

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">খোঁজের_প্যাটার্ন</span>`"`

- প্রতিটি ফাইলের ফাইল নাম এবং ম্যাচের সংখ্যা শুধু প্রিন্ট করুন:

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">খোঁজের_প্যাটার্ন</span>`"`

- `--type` দিয়ে ব্যবহার করা যাতে সমস্ত মানগুলি তালিকা:

`ack --help-types`
