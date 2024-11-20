---
layout: page
title: windows/expand (हिन्दी)
description: "विंडोज कैबिनेट फाइलों को अनकंप्रेस करें।"
content_hash: 137a5a57894b49b927ee64b73774111d7fd3fd5f
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/windows/expand.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/expand.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/expand.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/expand.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/expand.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># expand

विंडोज कैबिनेट फाइलों को अनकंप्रेस करें।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/expand>।

- एकल-फाइल कैबिनेट फाइल को निर्दिष्ट निर्देशिका में अनकंप्रेस करें:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल.cab/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निर्देशिका/का/पथ</span>

- स्रोत कैबिनेट फाइल में फाइलों की सूची प्रदर्शित करें:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल.cab/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निर्देशिका/का/पथ</span>` -d`

- कैबिनेट फाइल से सभी फाइलों को अनकंप्रेस करें:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल.cab/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निर्देशिका/का/पथ</span>` -f:*`

- कैबिनेट फाइल से एक विशेष फाइल को अनकंप्रेस करें:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल.cab/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निर्देशिका/का/पथ</span>` -f:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- अनकंप्रेस करते समय निर्देशिका संरचना की अनदेखी करें, और उन्हें एकल निर्देशिका में जोड़ें:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल.cab/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निर्देशिका/का/पथ</span>` -i`
