---
layout: page
title: linux/pacman-files (தமிழ்)
description: "ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு."
content_hash: 971023a9c651eafa04cf8b8015945c9da946a798
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-files.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-files.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-files.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pacman --files

ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு.
`pkgfile` ஐயும் பார்க்கவும்.
மேலும் விவரத்திற்கு: <https://man.archlinux.org/man/pacman.8>.

- தொகுப்பு தரவுத்தளத்தைப் புதுப்பிக்கவும்:

`sudo pacman --files --refresh`

- ஒரு குறிப்பிட்ட கோப்பை வைத்திருக்கும் தொகுப்பைக் கண்டறியவும்:

`pacman --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_பெயர்</span>

- வழக்கமான வெளிப்பாட்டைப் பயன்படுத்தி, ஒரு குறிப்பிட்ட கோப்பை வைத்திருக்கும் தொகுப்பைக் கண்டறியவும்:

`pacman --files --regex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வழக்கமான_வெளிப்பாடு</span>`'`

- தொகுப்பு பெயர்களை மட்டும் பட்டியலிடுங்கள்:

`pacman --files --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_பெயர்</span>

- குறிப்பிட்ட தொகுப்புக்கு சொந்தமான கோப்புகளை பட்டியலிடுங்கள்:

`pacman --files --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு_பெயர்</span>

- கோப்புகளுக்கான முழுமையான பாதையை மட்டும் பட்டியலிடுங்கள்:

`pacman --query --list --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு_பெயர்</span>

- உதவியைக் காட்டு:

`pacman --files --help`
