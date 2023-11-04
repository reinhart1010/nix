---
layout: page
title: linux/snap (বাংলা)
description: "\"স্ন্যাপ\" স্বয়ংসম্পূর্ণ সফটওয়্যার প্যাকেজসমুহ  পরিচালনার জন্য একটি টুল।"
content_hash: e457e880038ab5b24ce87243b6420d91cd9e0dac
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/linux/snap.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/snap.html
    icon: bi bi-globe
---
# snap

"স্ন্যাপ" স্বয়ংসম্পূর্ণ সফটওয়্যার প্যাকেজসমুহ  পরিচালনার জন্য একটি টুল।
এটি ".deb" এর জন্য `apt` এর অনুরূপ।
আরও তথ্য পাবেন: <https://manned.org/snap>.

- একটি প্যাকেজ অনুসন্ধান করুন:

`snap find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">প্যাকেজের_নাম</span>

- একটি প্যাকেজ ইনস্টল করুন:

`snap install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">প্যাকেজের_নাম</span>

- একটি প্যাকেজ আপডেট করুন:

`snap refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">প্যাকেজের_নাম</span>

- অন্য চ্যানেলে একটি প্যাকেজ আপডেট করুন (ট্র্যাক, রিস্ক বা ব্র্যাঞ্চ):

`snap refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">প্যাকেজের_নাম</span>` --channel=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">চ্যানেল</span>

- সমস্ত প্যাকেজ আপডেট করুন:

`snap refresh`

- ইনস্টল করা স্ন্যাপ সফটওয়্যার সম্পর্কে প্রাথমিক তথ্য প্রদর্শন করুন:

`snap list`

- একটি প্যাকেজ আনইনস্টল করুন:

`snap remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">প্যাকেজের_নাম</span>

- সিস্টেমে সাম্প্রতিক স্ন্যাপ পরিবর্তনের জন্য পরীক্ষা করুন:

`snap changes`
