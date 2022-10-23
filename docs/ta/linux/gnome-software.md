---
layout: page
title: linux/gnome-software (தமிழ்)
description: "பயன்பாடுகளைச் சேர்க்கவும் அகற்றவும் மற்றும் உங்கள் கணினியைப் புதுப்பிக்கவும்."
content_hash: 106b25b312cfa3da35ca9ae82d01390046f5c1a0
related_topics:
  - title: English version
    url: /en/linux/gnome-software.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gnome-software

பயன்பாடுகளைச் சேர்க்கவும் அகற்றவும் மற்றும் உங்கள் கணினியைப் புதுப்பிக்கவும்.
மேலும் விவரத்திற்கு: <https://apps.gnome.org/app/org.gnome.Software/>.

- GNOME மென்பொருள் GUI ஏற்கனவே இயங்கவில்லை என்றால் அதைத் தொடங்கவும்:

`gnome-software`

- GNOME மென்பொருள் GUI திறக்கப்படாவிட்டால் அதைத் துவக்கவும், மேலும் குறிப்பிட்ட பக்கத்திற்கு செல்லவும்:

`gnome-software --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">updates|updated|installed|overview</span>

- GNOME மென்பொருள் GUI திறக்கப்படாவிட்டால், அதைத் துவக்கி, குறிப்பிட்ட தொகுப்பைப் பார்க்கவும்:

`gnome-software --details `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுப்பு_பெயர்</span>

- பதிப்பைக் காட்டு:

`gnome-software --version`
