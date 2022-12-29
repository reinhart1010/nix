---
layout: page
title: linux/reboot (हिन्दी)
description: "मशीन को `reboot` करें"
content_hash: 2f15f95f269c811cacc50609e41ee38da910053c
last_modified_at: 2022-12-29
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
  - title: português (Brasil) version
    url: /pt_BR/linux/reboot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/reboot.html
    icon: bi bi-globe
---
# reboot

मशीन को `reboot` करें
अधिक जानकारी: <https://manned.org/reboot.8>।

- तुरंत पुनरारंभ करें:

`reboot`

- सिस्टम बंद करें ('पॉवरऑफ' के समान):

`reboot --poweroff`

- सिस्टम को रोकें (ठहराव के समान):

`reboot --halt`

- Sysadmin से संपर्क किए बिना तुरंत पुनरारंभ करें:

`reboot --force`

- सिस्टम को रिबूट किए बिना wtmp शटडाउन प्रविष्टि टाइप करें:

`reboot --wtmp-only`
