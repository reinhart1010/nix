---
layout: page
title: windows/path (हिन्दी)
description: "निष्पादन योग्य फ़ाइलों के लिए खोज पथ प्रदर्शित या सेट करें।"
content_hash: b41e79a15970a21439b991f478980db4c707984a
last_modified_at: 2023-11-06
related_topics:
  - title: বাংলা version
    url: /bn/windows/path.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/path.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/path.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/path.html
    icon: bi bi-globe
---
# path

निष्पादन योग्य फ़ाइलों के लिए खोज पथ प्रदर्शित या सेट करें।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/path>।

- वर्तमान पथ प्रदर्शित करें:

`path`

- एक या अधिक अर्धविराम से अलग की गई निर्देशिकाओं के लिए पथ सेट करें:

`path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ\से\निर्देशिका1 पथ\से\निर्देशिका2 ...</span>

- मूल पथ में एक नई निर्देशिका जोड़ें:

`path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ\से\निर्देशिका</span>`;%path%`

- निष्पादनयोग्यों के लिए केवल वर्तमान निर्देशिका को खोजने के लिए कमांड प्रॉम्प्ट सेट करें:

`path ;`
