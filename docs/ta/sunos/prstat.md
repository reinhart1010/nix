---
layout: page
title: sunos/prstat (தமிழ்)
description: "செயலில் உள்ள செயல்முறை புள்ளிவிவரங்களைப் புகாரளிக்கவும்."
content_hash: 0f5bd2d0fc87a8794e60d30e78b9fba83a073658
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/sunos/prstat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prstat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prstat

செயலில் உள்ள செயல்முறை புள்ளிவிவரங்களைப் புகாரளிக்கவும்.
மேலும் விவரத்திற்கு: <https://www.unix.com/man-page/sunos/1m/prstat>.

- CPU பயன்பாட்டின்படி வரிசைப்படுத்தப்பட்ட அனைத்து செயல்முறைகள் மற்றும் அறிக்கைகளின் புள்ளிவிவரங்களை ஆய்வு செய்யவும்:

`prstat`

- அனைத்து செயல்முறைகளையும் ஆய்வு செய்து, நினைவக பயன்பாட்டின்படி வரிசைப்படுத்தப்பட்ட புள்ளிவிவரங்களைப் புகாரளிக்கவும்:

`prstat -s rss`

- ஒவ்வொரு பயனருக்கும் மொத்த பயன்பாட்டுச் சுருக்கத்தைப் புகாரளிக்கவும்:

`prstat -t`

- மைக்ரோஸ்டேட் செயல்முறை கணக்கியல் தகவலைப் புகாரளிக்கவும்:

`prstat -m`

- ஒவ்வொரு நொடியும் செயல்முறைகளைப் பயன்படுத்தி முதல் 5 CPU இன் பட்டியலை அச்சிடவும்:

`prstat -c -n 5 -s cpu 1`
