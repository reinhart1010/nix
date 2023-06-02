---
layout: page
title: osx/launchd (தமிழ்)
description: "இது கணினி மற்றும் பயனர்களுக்கான செயல்முறைகளை நிர்வகிக்கிறது."
content_hash: 0a83c3c460f9149f86336ee8343f4a17ce5b1932
last_modified_at: 2023-06-02
related_topics:
  - title: العربية version
    url: /ar/osx/launchd.html
    icon: bi bi-globe
  - title: bosanski version
    url: /bs/osx/launchd.html
    icon: bi bi-globe
  - title: català version
    url: /ca/osx/launchd.html
    icon: bi bi-globe
  - title: dansk version
    url: /da/osx/launchd.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/osx/launchd.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/launchd.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/launchd.html
    icon: bi bi-globe
  - title: français version
    url: /fr/osx/launchd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/osx/launchd.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/launchd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/launchd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/osx/launchd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/osx/launchd.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/osx/launchd.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/osx/launchd.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/osx/launchd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/launchd.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/osx/launchd.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/launchd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/launchd.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/launchd.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/osx/launchd.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/osx/launchd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/osx/launchd.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/osx/launchd.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/osx/launchd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/launchd.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/osx/launchd.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/launchd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># launchd

இது கணினி மற்றும் பயனர்களுக்கான செயல்முறைகளை நிர்வகிக்கிறது.
கைமுறையாகத் `launchd` நீங்கள் அழைக்க முடியாது, அதனுடன் தொடர்பு கொள்ள `launchctl` ஐப் பயன்படுத்தவும்.
மேலும் விவரத்திற்கு: <https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html>.

- init ஐ இயக்கவும்:

`/sbin/launchd`

- `launchctl` ஐப் பயன்படுத்தி `launchd` உடன் தொடர்புகொள்வதற்கான ஆவணங்களைப் காண்க:

`tldr launchctl`
