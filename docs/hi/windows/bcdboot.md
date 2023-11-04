---
layout: page
title: windows/bcdboot (हिन्दी)
description: "बूट फ़ाइलों को कॉन्फ़िगर या सुधारें।"
content_hash: 7f2880c1c6f83299e66d3cb410dd08663c2b61c7
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/windows/bcdboot.html
    icon: bi bi-globe
---
# bcdboot

बूट फ़ाइलों को कॉन्फ़िगर या सुधारें।
अधिक जानकारी: <https://learn.microsoft.com/windows-hardware/manufacture/desktop/bcdboot-command-line-options-techref-di>.

- स्रोत विंडोज़ फ़ोल्डर से BCD फ़ाइलों का उपयोग करके सिस्टम विभाजन को प्रारंभ करें:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>

- वर्बोज़(verbose[v]) मोड सक्षम करें:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /v`

- सिस्टम विभाजन का वॉल्यूम अक्षर निर्दिष्ट करें:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">S:</span>

- कोई स्थान निर्दिष्ट करें:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en-us</span>

- बूट फ़ाइलों को निर्दिष्ट वॉल्यूम पर कॉपी करते समय फ़र्मवेयर प्रकार निर्दिष्ट करें:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">S:</span>` /f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UEFI|BIOS|ALL</span>
