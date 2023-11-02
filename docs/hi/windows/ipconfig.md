---
layout: page
title: windows/ipconfig (हिन्दी)
description: "विंडोज़ के नेटवर्क कॉन्फ़िगरेशन को प्रदर्शित और प्रबंधित करें।"
content_hash: 753a690621f69e9fcb2cc4712b90cf826931bb28
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/windows/ipconfig.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/ipconfig.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/ipconfig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/ipconfig.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/ipconfig.html
    icon: bi bi-globe
---
# ipconfig

विंडोज़ के नेटवर्क कॉन्फ़िगरेशन को प्रदर्शित और प्रबंधित करें।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>।

- नेटवर्क अडैप्टर की एक सूची दिखाएँ:

`ipconfig`

- नेटवर्क अडैप्टर की एक विस्तृत सूची दिखाएँ:

`ipconfig /all`

- नेटवर्क अडैप्टर के लिए आईपी पते नवीनीकृत करें:

`ipconfig /renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">अडैप्टर</span>

- नेटवर्क अडैप्टर के लिए आईपी पते खाली करें:

`ipconfig /release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">अडैप्टर</span>

- स्थानीय डीएनएस कैश दिखाएँ:

`ipconfig /displaydns`

- स्थानीय डीएनएस कैश से सभी डेटा हटाएँ:

`ipconfig /flushdns`
