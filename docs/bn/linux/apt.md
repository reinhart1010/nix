---
layout: page
title: linux/apt (বাংলা)
description: "ডেবিয়ান ভিত্তিক ডিস্ট্রিবিউশনের জন্য প্যাকেজ ম্যানেজমেন্ট ইউটিলিটি।"
content_hash: bc82bab12200863c2dcd02ab8987d286c5515e3a
last_modified_at: 2023-11-06
related_topics:
  - title: العربية version
    url: /ar/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
---
# apt

ডেবিয়ান ভিত্তিক ডিস্ট্রিবিউশনের জন্য প্যাকেজ ম্যানেজমেন্ট ইউটিলিটি।
ইন্টারেক্টিভভাবে ব্যবহৃত হলে উবুন্টু সংস্করণ 16.04 এবং তার পরবর্তী সংস্করনের জন্য `apt-get` এর পরিবরতে রেকোমেন্ডেড প্রতিস্থাপন।
আরও তথ্য পাবেন: <https://manpages.debian.org/latest/apt/apt.8.html>।

- উপলভ্য প্যাকেজ এবং সংস্করণের তালিকা আপডেট করুন (অন্যান্য `apt` কমান্ডের আগে এটি চালানোর পরামর্শ দেওয়া হচ্ছে):

`sudo apt update`

- প্রদত্ত প্যাকেজ অনুসন্ধান করুন:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">প্যাকেজ</span>

- একটি প্যাকেজের জন্য তথ্য দেখান:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">প্যাকেজ</span>

- একটি প্যাকেজ ইনস্টল করুন, অথবা সর্বশেষ উপলব্ধ সংস্করণে আপডেট করুন:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">প্যাকেজ</span>

- একটি প্যাকেজ সরান (পরিবর্তে `purge` ব্যবহার করে এর কনফিগারেশন ফাইলও সরিয়ে দেয়):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">প্যাকেজ</span>

- সমস্ত ইনস্টল করা প্যাকেজগুলি তাদের নতুন উপলব্ধ সংস্করণগুলিতে আপগ্রেড করুন:

`sudo apt upgrade`

- সমস্ত প্যাকেজের তালিকা করুন:

`apt list`

- ইনস্টল করা প্যাকেজ সমূহ তালিকা করুন:

`apt list --installed`
