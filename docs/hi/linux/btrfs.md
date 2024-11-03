---
layout: page
title: linux/btrfs (हिन्दी)
description: "लिनक्स के लिए कॉपी-ऑन-राइट (COW) सिद्धांत पर आधारित एक फ़ाइल सिस्टम।"
content_hash: f93e65d20d9576593536a71635bddee2fb470beb
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/linux/btrfs.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/btrfs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/btrfs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs

लिनक्स के लिए कॉपी-ऑन-राइट (COW) सिद्धांत पर आधारित एक फ़ाइल सिस्टम।
कुछ सब-कमांड जैसे `btrfs device`, उनका खुद का उपयोग दस्तावेज़न है।
अधिक जानकारी: <https://btrfs.readthedocs.io/en/latest/btrfs.html>।

- उप-वॉल्यूम बनाएं:

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उप-वॉल्यूम/का/पथ</span>

- उप-वॉल्यूमों की सूची दिखाएं:

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">माउंट_बिंदु/का/पथ</span>

- स्थान उपयोग सूचना दिखाएं:

`sudo btrfs filesystem df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">माउंट_बिंदु/का/पथ</span>

- कोटा सक्षम करें:

`sudo btrfs quota enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उप-वॉल्यूम/का/पथ</span>

- कोटा दिखाएं:

`sudo btrfs qgroup show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उप-वॉल्यूम/का/पथ</span>
