---
layout: page
title: linux/reboot (हिन्दी)
description: "मशीन को `reboot` करें"
content_hash: 5bbcd8f2865f9733b1a461e77a1ae618d0f56b8c
related_topics:
  - title: català version
    url: /ca/linux/reboot.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/reboot.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/reboot.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/reboot.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/reboot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/reboot.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># reboot

मशीन को `reboot` करें
अधिक जानकारी: <https://www.man7.org/linux/man-pages/man8/reboot.8.html>.

- तुरंत पुनरारंभ करें:

`reboot`

- सिस्टम बंद करें ('पॉवरऑफ' के समान):

`reboot --poweroff`

- सिस्टम को रोकें (ठहराव के समान):

`reboot --halt`

- Sysadmin से संपर्क किए बिना तुरंत पुनरारंभ करें:

`reboot --force --force`

- सिस्टम को रिबूट किए बिना wtmp शटडाउन प्रविष्टि टाइप करें:

`reboot --wtmp-only`
