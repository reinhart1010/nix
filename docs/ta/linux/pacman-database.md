---
layout: page
title: linux/pacman-database (தமிழ்)
description: "ஆர்ச் லினக்ஸ் தொகுப்பு தரவுத்தளத்தில் செயல்படவும்."
content_hash: 0d1044f3c88ba2c223c27025c6aec7fb8d846ff1
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-database.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-database.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-database.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pacman --database

ஆர்ச் லினக்ஸ் தொகுப்பு தரவுத்தளத்தில் செயல்படவும்.
நிறுவப்பட்ட தொகுப்புகளின் சில பண்புகளை மாற்றவும்.
மேலும் விவரத்திற்கு: <https://man.archlinux.org/man/pacman.8>.

- ஒரு தொகுப்பை மறைமுகமாக நிறுவியதாகக் குறிக்கவும்:

`sudo pacman --database --asdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு_பெயர்</span>

- ஒரு தொகுப்பை வெளிப்படையாக நிறுவியதாகக் குறிக்கவும்:

`sudo pacman --database --asexplicit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு_பெயர்</span>

- அனைத்து தொகுப்பு சார்புகளும் நிறுவப்பட்டுள்ளதா என சரிபார்க்கவும்:

`pacman --database --check`

- அனைத்து குறிப்பிட்ட சார்புகளும் உள்ளனவா என்பதை உறுதிசெய்ய, களஞ்சியங்களைச் சரிபார்க்கவும்:

`pacman --database --check --check`

- பிழை செய்திகளை மட்டும் காட்டு:

`pacman --database --check --quiet`

- உதவியைக் காட்டு:

`pacman --database --help`
