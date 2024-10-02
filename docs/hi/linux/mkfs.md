---
layout: page
title: linux/mkfs (हिन्दी)
description: "एक हार्ड डिस्क पार्टीशन पर लिनक्स फाइल सिस्टम बनाएं।"
content_hash: b38a9c2428037b0a41f693b9b5caeac52ed90413
last_modified_at: 2024-10-02
related_topics:
  - title: English version
    url: /en/linux/mkfs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/mkfs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/mkfs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/mkfs.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mkfs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkfs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkfs

एक हार्ड डिस्क पार्टीशन पर लिनक्स फाइल सिस्टम बनाएं।
यह कमांड अब अप्रचलित है, और इसके स्थान पर फाइल सिस्टम विशेष mkfs.<type> यूटिलिटीज़ का उपयोग करें।
अधिक जानकारी: <https://manned.org/mkfs>।

- एक पार्टीशन पर लिनक्स ext2 फाइल सिस्टम बनाएं:

`mkfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- निर्दिष्ट प्रकार का फाइल सिस्टम बनाएं:

`mkfs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ext4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- निर्दिष्ट प्रकार का फाइल सिस्टम बनाएं और खराब ब्लॉक्स के लिए जांच करें:

`mkfs -c -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>
