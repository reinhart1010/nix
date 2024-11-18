---
layout: page
title: windows/psversiontable (हिन्दी)
description: "वर्तमान PowerShell संस्करण प्राप्त करने के लिए एक केवल-पढ़ने योग्य चर (जैसे `$PSVersionTable`)।"
content_hash: 5666915f923377e29ffb24505d301b1dc15b5385
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/windows/psversiontable.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/psversiontable.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/psversiontable.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># PSVersionTable

वर्तमान PowerShell संस्करण प्राप्त करने के लिए एक केवल-पढ़ने योग्य चर (जैसे `$PSVersionTable`)।
यह कमांड केवल PowerShell के तहत चलाया जा सकता है।
अधिक जानकारी: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_automatic_variables#psversiontable>।

- वर्तमान में स्थापित PowerShell संस्करण और संस्करण का एक सारांश प्रिंट करें:

`$PSVersionTable`

- PowerShell का विस्तृत (मुख्य, उप, निर्माण, और संशोधन) संस्करण संख्या प्राप्त करें:

`$PSVersionTable.PSVersion`

- सभी समर्थित PowerShell स्क्रिप्ट संस्करणों की सूची बनाएं जिन्हें यह PowerShell संस्करण समर्थन करता है:

`$PSVersionTable.PSCompatibleVersions`

- नवीनतम Git कमिट ID प्राप्त करें जिस पर वर्तमान में स्थापित PowerShell संस्करण आधारित है (PowerShell 6.0 और बाद के संस्करण पर कार्य करता है):

`$PSVersionTable.GitCommitId`

- जांचें कि क्या उपयोगकर्ता PowerShell Core (6.0 या बाद के संस्करण) चला रहा है या मूल "Windows PowerShell" (संस्करण 5.1 या उससे नीचे):

`$PSVersionTable.PSEdition`
