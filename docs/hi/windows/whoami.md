---
layout: page
title: windows/whoami (हिन्दी)
description: "वर्तमान उपयोगकर्ता के बारे में विवरण प्रदर्शित करें।"
content_hash: 62b41ef3e1c28a3f97ce05efdce9c25f0ce9b4ed
last_modified_at: 2024-11-26
related_topics:
  - title: English version
    url: /en/windows/whoami.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/whoami.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/whoami.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/whoami.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/whoami.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/whoami.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/whoami.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/whoami.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/whoami.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/whoami.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/whoami.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># whoami

वर्तमान उपयोगकर्ता के बारे में विवरण प्रदर्शित करें।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/whoami>।

- वर्तमान उपयोगकर्ता का उपयोगकर्ता नाम प्रदर्शित करें:

`whoami`

- वर्तमान उपयोगकर्ता जिन समूहों का सदस्य है, उन्हें प्रदर्शित करें:

`whoami /groups`

- वर्तमान उपयोगकर्ता के विशेषाधिकार प्रदर्शित करें:

`whoami /priv`

- वर्तमान उपयोगकर्ता का उपयोगकर्ता प्रधान नाम (UPN) प्रदर्शित करें:

`whoami /upn`

- वर्तमान उपयोगकर्ता का लॉगिन ID प्रदर्शित करें:

`whoami /logonid`

- वर्तमान उपयोगकर्ता के लिए सभी जानकारी प्रदर्शित करें:

`whoami /all`
