---
layout: page
title: windows/fc (हिन्दी)
description: "दो फ़ाइलों या फ़ाइलों के सेट के बीच के अंतर की तुलना करें।"
content_hash: b6d6eac63f1486ebdf0ae64bcfb5a00a40d74af6
last_modified_at: 2024-11-26
related_topics:
  - title: English version
    url: /en/windows/fc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/fc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/fc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/fc.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/fc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/fc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fc

दो फ़ाइलों या फ़ाइलों के सेट के बीच के अंतर की तुलना करें।
फ़ाइलों के सेट की तुलना करने के लिए वाइल्डकार्ड (\*) का उपयोग करें।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/fc>।

- 2 निर्दिष्ट फ़ाइलों की तुलना करें:

`fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल1\का\पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल2\का\पथ</span>

- केस-इंसेंसिटिव तुलना करें:

`fc /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल1\का\पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल2\का\पथ</span>

- फ़ाइलों की तुलना यूनिकोड टेक्स्ट के रूप में करें:

`fc /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल1\का\पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल2\का\पथ</span>

- फ़ाइलों की तुलना ASCII टेक्स्ट के रूप में करें:

`fc /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल1\का\पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल2\का\पथ</span>

- फ़ाइलों की तुलना बाइनरी के रूप में करें:

`fc /b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल1\का\पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल2\का\पथ</span>

- टैब-से-स्पेस विस्तार को अक्षम करें:

`fc /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल1\का\पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल2\का\पथ</span>

- तुलना के लिए व्हाइटस्पेस (टैब और स्पेस) को संकुचित करें:

`fc /w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल1\का\पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल2\का\पथ</span>
