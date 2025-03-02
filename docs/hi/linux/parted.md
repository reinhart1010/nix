---
layout: page
title: linux/parted (हिन्दी)
description: "एक पार्टीशन मैनिपुलेशन प्रोग्राम।"
content_hash: 396830ef68e842d47aaf26ee72d6a15e1f553a30
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/parted.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/parted.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/parted.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># parted

एक पार्टीशन मैनिपुलेशन प्रोग्राम।
देखें भी: `partprobe`.
अधिक जानकारी: <https://www.gnu.org/software/parted/parted.html>।

- सभी ब्लॉक डिवाइस पर पार्टीशनों की सूची दिखाएं:

`sudo parted --list`

- निर्दिष्ट डिस्क के साथ इंटरैक्टिव मोड शुरू करें:

`sudo parted `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- निर्दिष्ट लेबल-प्रकार का नया पार्टीशन टेबल बनाएं:

`sudo parted --script `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>` mklabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun</span>

- इंटरैक्टिव मोड में पार्टीशन की जानकारी दिखाएं:

`print`

- इंटरैक्टिव मोड में डिस्क का चयन करें:

`select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- इंटरैक्टिव मोड में निर्दिष्ट फ़ाइल सिस्टम के साथ 16 जीबी का पार्टीशन बनाएं:

`mkpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primary|logical|extended</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16G</span>

- इंटरैक्टिव मोड में पार्टीशन का आकार बदलें:

`resizepart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पार्टीशन की अंतिम स्थिति</span>

- इंटरैक्टिव मोड में एक पार्टीशन को हटाएं:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
