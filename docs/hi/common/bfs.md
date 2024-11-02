---
layout: page
title: common/bfs (हिन्दी)
description: "अपनी फ़ाइलों के लिए चौड़ाई-प्रथम खोज।"
content_hash: ccf4115640fa737cb1a2d2eb3a2095b503f74bd5
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/bfs.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bfs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bfs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bfs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bfs

अपनी फ़ाइलों के लिए चौड़ाई-प्रथम खोज।
अधिक जानकारी: <https://manned.org/bfs>।

- एक्सटेंशन द्वारा फ़ाइलें ढूंढें:

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रूट_पथ</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`'`

- एकाधिक पथ/नाम पैटर्न से मेल खाने वाली फ़ाइलें ढूंढें:

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रूट_पथ</span>` -path '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">**/पथ/**/*.ext</span>`' -or -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*पैटर्न*</span>`'`

- केस-असंवेदनशील मोड में, किसी दिए गए नाम से मेल खाने वाली निर्देशिकाएँ खोजें:

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रूट_पथ</span>` -type d -iname '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*lib*</span>`'`

- विशिष्ट पथों को छोड़कर, किसी दिए गए पैटर्न से मेल खाने वाली फ़ाइलें ढूंढें:

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रूट_पथ</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.py</span>`' -not -path '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/साइट-पैकेज/*</span>`'`

- किसी दिए गए आकार सीमा से मेल खाने वाली फ़ाइलें ढूंढें, पुनरावर्ती गहराई को "1" तक सीमित करें:

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रूट_पथ</span>` -maxdepth 1 -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+500k</span>` -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10M</span>

- प्रत्येक फ़ाइल के लिए एक कमांड चलाएँ (फ़ाइल नाम तक पहुँचने के लिए कमांड के भीतर `{}` का उपयोग करें):

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रूट_पथ</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`' -exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l</span>` {} \;`

- आज संशोधित सभी फ़ाइलें ढूंढें और परिणामों को तर्क के रूप में एकल कमांड में पास करें:

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रूट_पथ</span>` -daystart -mtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1</span>` -exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tar -cvf archive.tar</span>` {} \+`

- खाली फ़ाइलें (0 बाइट) या निर्देशिकाएं ढूंढें और उन्हें शब्दशः हटाएं:

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रूट_पथ</span>` -type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f|d</span>` -empty -delete -print`
