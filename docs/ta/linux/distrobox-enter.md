---
layout: page
title: linux/distrobox-enter (தமிழ்)
description: "டிஸ்ட்ரோபாக்ஸ் கொள்கலனில் கட்டளையை இயக்கவும்."
content_hash: b1e40db58cde1d6d9ee621ace1945405bca3b92a
related_topics:
  - title: English version
    url: /en/linux/distrobox-enter.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># distrobox-enter

டிஸ்ட்ரோபாக்ஸ் கொள்கலனில் கட்டளையை இயக்கவும்.
முன்னிருப்பு கட்டளை செயல்படுத்தப்பட்டது உங்கள் ஷெல் ஆகும், இயக்குவதற்கு வெவ்வேறு ஷெல்கள் அல்லது முழு கட்டளைகளையும் குறிப்பிடவும். ஸ்கிரிப்ட், பயன்பாடு அல்லது சேவையில் பயன்படுத்தினால், tty மற்றும் ஊடாடும் தன்மையை முடக்க --headless பயன்முறையைக் குறிப்பிடலாம்.
மேலும் விவரத்திற்கு: <https://distrobox.privatedns.org>.

- ஒரு டிஸ்ட்ரோபாக்ஸை உள்ளிட்டு, `sh -l` ஐ இயக்கவும்:

`distrobox-enter container-name -- sh -l`

- ஒரு tty ஐ உடனடியாகச் செய்யாமல் ஒரு டிஸ்ட்ரோபாக்ஸை உள்ளிடவும்:

`distrobox-enter -H container-name -- uptime -p`
