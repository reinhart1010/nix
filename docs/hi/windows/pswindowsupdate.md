---
layout: page
title: windows/pswindowsupdate (हिन्दी)
description: "Windows Update प्रबंधित करने के लिए एक PowerShell बाहरी मॉड्यूल।"
content_hash: 7b61a4c22a07054cf18668e58bc3528aef55ffa5
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/windows/pswindowsupdate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/pswindowsupdate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/pswindowsupdate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># PSWindowsUpdate

Windows Update प्रबंधित करने के लिए एक PowerShell बाहरी मॉड्यूल।
यह उपकरण कई कमांड प्रदान करता है जिन्हें केवल PowerShell के माध्यम से चलाया जा सकता है।
अधिक जानकारी: <https://github.com/mgajda83/PSWindowsUpdate>।

- मॉड्यूल को `Install-Module` का उपयोग करके स्थापित करें:

`Install-Module PSWindowsUpdate`

- मॉड्यूल के अंतर्गत सभी उपलब्ध कमांडों की सूची बनाएं:

`Get-Command -Module PSWindowsUpdate`
