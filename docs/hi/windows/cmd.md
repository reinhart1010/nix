---
layout: page
title: windows/cmd (हिन्दी)
description: "विंडोज कमांड दुभाषिया।"
content_hash: 4644d96f1421df595e4450b8e7eff99c144bb2fe
related_topics:
  - title: English version
    url: /en/windows/cmd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cmd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cmd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cmd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/cmd.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cmd

विंडोज कमांड दुभाषिया।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>।

- एक इंटरैक्टिव शेल सत्र प्रारंभ करें:

`cmd`

- एक आदेश निष्पादित करें:

`cmd /c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आज्ञा</span>`"`

- एक स्क्रिप्ट निष्पादित करें:

`cmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल.bat/का/पथ</span>

- एक कमांड निष्पादित करें और फिर एक इंटरेक्टिव शेल दर्ज करें:

`cmd /k "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आज्ञा</span>`"`

- एक इंटरैक्टिव शेल सत्र प्रारंभ करें जहां कमांड आउटपुट में `echo` अक्षम है:

`cmd /q`

- विलंबित चर विस्तार सक्षम या अक्षम के साथ एक इंटरैक्टिव शेल सत्र प्रारंभ करें:

`cmd /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- सक्षम या अक्षम कमांड एक्सटेंशन के साथ एक इंटरैक्टिव शेल सत्र प्रारंभ करें:

`cmd /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- प्रयुक्त यूनिकोड एन्कोडिंग के साथ एक इंटरैक्टिव शेल सत्र प्रारंभ करें:

`cmd /u`
