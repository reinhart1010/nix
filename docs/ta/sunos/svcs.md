---
layout: page
title: sunos/svcs (தமிழ்)
description: "இயங்கும் சேவைகள் பற்றிய தகவல்களை பட்டியலிடுங்கள்."
content_hash: 1bdf2927332c79e87a944737f8b013b038331d17
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/sunos/svcs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/svcs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svcs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# svcs

இயங்கும் சேவைகள் பற்றிய தகவல்களை பட்டியலிடுங்கள்.
மேலும் விவரத்திற்கு: <https://www.unix.com/man-page/linux/1/svcs>.

- இயங்கும் அனைத்து சேவைகளையும் பட்டியலிடுங்கள்:

`svcs`

- இயங்காத சேவைகளை பட்டியலிடுங்கள்:

`svcs -vx`

- சேவையைப் பற்றிய தகவல்களைப் பட்டியலிடுங்கள்:

`svcs apache`

- சேவை பதிவு கோப்பின் இருப்பிடத்தைக் காட்டு:

`svcs -L apache`

- சேவை பதிவு கோப்பின் முடிவைக் காண்பி:

`tail $(svcs -L apache)`
