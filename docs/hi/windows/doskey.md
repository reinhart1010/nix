---
layout: page
title: windows/doskey (हिन्दी)
description: "मैक्रोज़, विंडोज़ कमांड और कमांड-लाइन प्रबंधित करें।"
content_hash: 7c4a7340aaf2d5c945d71e9946111a30fcd71124
last_modified_at: 2023-11-04
related_topics:
  - title: বাংলা version
    url: /bn/windows/doskey.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/doskey.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/doskey.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/doskey.html
    icon: bi bi-globe
---
# doskey

मैक्रोज़, विंडोज़ कमांड और कमांड-लाइन प्रबंधित करें।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/doskey>.

- उपलब्ध मैक्रोज़ की सूची बनाएं:

`doskey /macros`

- एक नया मैक्रो बनाएं:

`doskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आज्ञा</span>`"`

- किसी विशिष्ट निष्पादन योग्य के लिए एक नया मैक्रो बनाएं:

`doskey /exename=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निष्पादन</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आज्ञा</span>`"`

- मैक्रो हटाएँ:

`doskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>` =`

- मेमोरी में संग्रहीत सभी कमांड प्रदर्शित करें:

`doskey /history`

- पोर्टेबिलिटी के लिए मैक्रोज़ को फ़ाइल में सहेजें:

`doskey /macros > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">मैकिनिट_फ़ाइल\का\पथ</span>

- किसी फ़ाइल से मैक्रोज़ लोड करें:

`doskey /macrofile = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">मैकिनिट_फ़ाइल\का\पथ</span>
