---
layout: page
title: windows/cmstp (हिन्दी)
description: "कनेक्शन सेवा प्रोफाइल प्रबंधित करें।"
content_hash: a4fa83c152e76f8ec37c0ce605c284cba3b5781e
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/windows/cmstp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/cmstp.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cmstp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cmstp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/cmstp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cmstp

कनेक्शन सेवा प्रोफाइल प्रबंधित करें।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmstp>।

- एक विशेष प्रोफाइल स्थापित करें:

`cmstp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रोफ़ाइल_फ़ाइल\का\पथ</span>`"`

- डेस्कटॉप शॉर्टकट बनाए बिना स्थापित करें:

`cmstp /ns "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रोफ़ाइल_फ़ाइल\का\पथ</span>`"`

- निर्भरताओं की जांच किए बिना स्थापित करें:

`cmstp /nf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रोफ़ाइल_फ़ाइल\का\पथ</span>`"`

- केवल वर्तमान उपयोगकर्ता के लिए स्थापित करें:

`cmstp /su "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रोफ़ाइल_फ़ाइल\का\पथ</span>`"`

- सभी उपयोगकर्ताओं के लिए स्थापित करें (प्रशासक विशेषाधिकार की आवश्यकता है):

`cmstp /au "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रोफ़ाइल_फ़ाइल\का\पथ</span>`"`

- बिना किसी संकेत के चुपचाप स्थापित करें:

`cmstp /s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रोफ़ाइल_फ़ाइल\का\पथ</span>`"`

- एक विशेष प्रोफाइल अनइंस्टॉल करें:

`cmstp /u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रोफ़ाइल_फ़ाइल\का\पथ</span>`"`

- बिना पुष्टि संकेत के चुपचाप अनइंस्टॉल करें:

`cmstp /u /s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रोफ़ाइल_फ़ाइल\का\पथ</span>`"`
