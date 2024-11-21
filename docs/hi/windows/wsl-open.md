---
layout: page
title: windows/wsl-open (हिन्दी)
description: "Windows सबसिस्टम फॉर लिनक्स के भीतर से एक फ़ाइल या URL को उपयोगकर्ता के डिफ़ॉल्ट Windows GUI एप्लिकेशन में खोलें।"
content_hash: bf584c2b60232429ec1df7a8ea6168a8590dba96
last_modified_at: 2024-11-21
related_topics:
  - title: English version
    url: /en/windows/wsl-open.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/wsl-open.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/wsl-open.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wsl-open

Windows सबसिस्टम फॉर लिनक्स के भीतर से एक फ़ाइल या URL को उपयोगकर्ता के डिफ़ॉल्ट Windows GUI एप्लिकेशन में खोलें।
अधिक जानकारी: <https://gitlab.com/4U6U57/wsl-open>।

- वर्तमान निर्देशिका को Windows एक्सप्लोरर में खोलें:

`wsl-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- उपयोगकर्ता के डिफ़ॉल्ट वेब ब्राउज़र में एक URL खोलें:

`wsl-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- उपयोगकर्ता के डिफ़ॉल्ट एप्लिकेशन में एक विशेष फ़ाइल खोलें:

`wsl-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल\का\पथ</span>

- `wsl-open` को शेल के वेब ब्राउज़र के रूप में सेट करें (लिंक को `wsl-open` के साथ खोलें):

`wsl-open -w`

- मदद दिखाएं:

`wsl-open -h`
