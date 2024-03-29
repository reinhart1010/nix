---
layout: page
title: common/a2ping (বাংলা)
description: "চিত্রগুলি কে EPS বা PDF ফাইলে রূপান্তর করুন।"
content_hash: 18af7125a4b1e521062e408c77d7ed08e8921734
last_modified_at: 2023-11-19
related_topics:
  - title: English version
    url: /en/common/a2ping.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/a2ping.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/a2ping.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/a2ping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# a2ping

চিত্রগুলি কে EPS বা PDF ফাইলে রূপান্তর করুন।
আরও তথ্য পাবেন: <https://manned.org/a2ping>।

- একটি চিত্রকে PDF তে রূপান্তর করুন (নোট: আউটপুট ফাইল নাম নির্দিষ্ট করা ঐচ্ছিক):

`a2ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">চিত্র.ext/এর/পথ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">আউটপুট.pdf/এর/পথ</span>

- নির্দিষ্ট শৈলীতে ডকুমেন্ট সংক্ষিপ্ত করুন:

`a2ping --nocompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|zip|best|flate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইল/এর/পথ</span>

- যদি উচ্চ রেজোলিউশন বাক্স স্ক্যান করা থাকে তবে HiResBoundingBox (নোট: এটি ডিফল্টভাবে হ্যাঁ):

`a2ping --nohires `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইল/এর/পথ</span>

- মূল পৃষ্ঠার নিচে এবং বামে পৃষ্ঠার কন্টেন্টের অনুমতি দিন (নোট: এটি ডিফল্টভাবে না):

`a2ping --below `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইল/এর/পথ</span>

- `gs` এর জন্য অতিরিক্ত আর্গুমেন্ট পাস করুন:

`a2ping --gsextra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">আর্গুমেন্ট</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইল/এর/পথ</span>

- বাহ্যিক প্রোগ্রামে অতিরিক্ত আর্গুমেন্ট পাস করুন (যেমন `pdftops`):

`a2ping --extra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">আর্গুমেন্ট</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ফাইল/এর/পথ</span>

- সাহায্য প্রদর্শন করুন:

`a2ping -h`
