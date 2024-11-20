---
layout: page
title: windows/choco-pack (हिन्दी)
description: "एक NuGet विनिर्देशन को `nupkg` फ़ाइल में पैक करें।"
content_hash: 8cc1a8e4e02364027716580dec310bb334366406
last_modified_at: 2024-11-20
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-pack.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-pack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/choco-pack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-pack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-pack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-pack.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/choco-pack.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># choco pack

एक NuGet विनिर्देशन को `nupkg` फ़ाइल में पैक करें।
अधिक जानकारी: <https://chocolatey.org/docs/commands-pack>।

- एक NuGet विनिर्देशन को `nupkg` फ़ाइल में पैक करें:

`choco pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">विशिष्टता_फ़ाइल\का\पथ</span>

- परिणामी फ़ाइल के संस्करण को निर्दिष्ट करते हुए एक NuGet विनिर्देशन को पैक करें:

`choco pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">विशिष्टता_फ़ाइल\का\पथ</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संस्करण</span>

- एक विशेष निर्देशिका में NuGet विनिर्देशन को पैक करें:

`choco pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">विशिष्टता_फ़ाइल\का\पथ</span>` --output-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट_डायरेक्टरी\का\पथ</span>
