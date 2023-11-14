---
layout: page
title: linux/pacman-deptest (தமிழ்)
description: "குறிப்பிடப்பட்ட ஒவ்வொரு சார்புநிலையையும் சரிபார்த்து, கணினியில் தற்போது திருப்தி அடையாத சார்புகளின் பட்டியலைத் திருப்பி அனுப்பவும்."
content_hash: c6a23f69c984dbdd8b798426c75b3b76fed0fd22
last_modified_at: 2023-11-14
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-deptest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --deptest

குறிப்பிடப்பட்ட ஒவ்வொரு சார்புநிலையையும் சரிபார்த்து, கணினியில் தற்போது திருப்தி அடையாத சார்புகளின் பட்டியலைத் திருப்பி அனுப்பவும்.
இதையும் பார்க்கவும்: `pacman`.
மேலும் விவரத்திற்கு: <https://man.archlinux.org/man/pacman.8>.

- நிறுவப்படாத சார்புகளின் தொகுப்பு பெயர்களை அச்சிடவும்:

`pacman --deptest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு1 நிரல்தொகுப்பு2 ...</span>

- நிறுவப்பட்ட தொகுப்பு கொடுக்கப்பட்ட குறைந்தபட்ச பதிப்பை பூர்த்திசெய்கிறதா என சரிபார்க்கவும்:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>=5</span>`"`

- தொகுப்பின் பிந்தைய பதிப்பு நிறுவப்பட்டுள்ளதா எனச் சரிபார்க்கவும்:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>5</span>`"`

- உதவியைக் காட்டு:

`pacman --deptest --help`
