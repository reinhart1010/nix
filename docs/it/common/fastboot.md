---
layout: page
title: common/fastboot (italiano)
description: "Comunica con il dispositivo Android connessione quando in modalità bootloader (la situazione in cui `adb` non funziona)."
content_hash: 60577282ece6cdd5abd2f537322a2e204f28f254
last_modified_at: 2023-10-21
related_topics:
  - title: English version
    url: /en/common/fastboot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fastboot.html
    icon: bi bi-globe
---
# fastboot

Comunica con il dispositivo Android connessione quando in modalità bootloader (la situazione in cui `adb` non funziona).
Maggiori informazioni: <https://cs.android.com/android/platform/superproject/+/main:system/core/fastboot>.

- Sblocca il bootloader:

`fastboot oem unlock`

- Ri-blocca il bootloader:

`fastboot oem lock`

- Riavvia il dispositivo da modalità fastboot, nuovamente in modalità fastboot:

`fastboot reboot bootloader`

- Esegue in Flash di una data immagine:

`fastboot flash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.img</span>

- Esegue il Flash di una recovery image personalizzata:

`fastboot flash recovery `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.img</span>

- Mostra i dispositivi connessi:

`fastboot devices`

- Mostra tutte le informazioni su un dispositivo:

`fastboot getvar all`
