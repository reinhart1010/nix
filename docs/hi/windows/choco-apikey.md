---
layout: page
title: windows/choco-apikey (हिन्दी)
description: "चॉकलेट के स्रोतों के लिए एपीआई की प्रबंधित करें।"
content_hash: 4e0c5e743856a987a627ec6673c63ab6ddeb3a39
last_modified_at: 2024-11-20
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-apikey.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-apikey.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/choco-apikey.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/choco-apikey.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/choco-apikey.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-apikey.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-apikey.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/choco-apikey.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># choco apikey

चॉकलेट के स्रोतों के लिए एपीआई की प्रबंधित करें।
अधिक जानकारी: <https://chocolatey.org/docs/commands-apikey>।

- स्रोतों और उनके API चाबी की सूची दिखाएं:

`choco apikey`

- एक विशिष्ट स्रोत और उसके API चाबी को दिखाएं:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत_URL</span>`"`

- एक स्रोत के लिए API चाबी सेट करें:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत_URL</span>`" --key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_चाबी</span>`"`

- एक स्रोत के लिए API चाबी हटाएं:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत_URL</span>`" --remove`
