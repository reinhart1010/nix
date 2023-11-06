---
layout: page
title: common/aireplay-ng (বাংলা)
description: "ওয়ায়ারলেস নেটওয়ার্কে প্যাকেট ইনজেক্ট করুন।"
content_hash: 844c8c9030b00b73c071e5d493645b5978b6959f
last_modified_at: 2023-11-06
related_topics:
  - title: Deutsch version
    url: /de/common/aireplay-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aireplay-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aireplay-ng.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/aireplay-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/aireplay-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aireplay-ng.html
    icon: bi bi-globe
---
# aireplay-ng

ওয়ায়ারলেস নেটওয়ার্কে প্যাকেট ইনজেক্ট করুন।
`aireplay-ng` এর একটি অংশ।
আরও তথ্য পাবেন: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>।

- একটি এক্সেস পয়েন্টের MAC ঠিকানা, ক্লায়েন্টের MAC ঠিকানা এবং একটি ইন্টারফেস দেখে একটি নির্দিষ্ট সংখ্যক অপ্রাপ্ত প্যাকেট পাঠান:

`sudo aireplay-ng --deauth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">গণনা</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` --dmac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client_mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ইন্টারফেস</span>
