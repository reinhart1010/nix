---
layout: page
title: linux/btrfs (हिन्दी)
description: "लिनक्स के लिए कॉपी-ऑन-राइट (COW) सिद्धांत पर आधारित एक फ़ाइल सिस्टम।"
content_hash: cf4939ec6dd8d2b4d108fe79936b880c425c517c
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/linux/btrfs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs.html
    icon: bi bi-globe
---
# btrfs

लिनक्स के लिए कॉपी-ऑन-राइट (COW) सिद्धांत पर आधारित एक फ़ाइल सिस्टम।
कुछ सब-कमांड जैसे `btrfs device`, उनका खुद का उपयोग दस्तावेज़न है।
अधिक जानकारी: <https://btrfs.readthedocs.io/en/latest/btrfs.html>।

- उप-वॉल्यूम बनाएं:

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/उप-वॉल्यूम</span>

- उप-वॉल्यूमों की सूची दिखाएं:

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/माउंट_बिंदु</span>

- स्थान उपयोग सूचना दिखाएं:

`sudo btrfs filesystem df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/माउंट_बिंदु</span>

- कोटा सक्षम करें:

`sudo btrfs quota enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/उप-वॉल्यूम</span>

- कोटा दिखाएं:

`sudo btrfs qgroup show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/उप-वॉल्यूम</span>
