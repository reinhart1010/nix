---
layout: page
title: osx/diskutil (italiano)
description: "Strumento per gestire i dischi locali e i volumi."
content_hash: b215551d23a33e425a45be06a63589b49a7b9c84
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/osx/diskutil.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/diskutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/diskutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/diskutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/diskutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diskutil

Strumento per gestire i dischi locali e i volumi.
Maggiori informazioni: <https://ss64.com/osx/diskutil.html>.

- Mostra tutti i dischi correnti, le partizioni e i volumi montati:

`diskutil list`

- Ripara le strutture dati del filesystem di un volume:

`diskutil repairVolume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/diskX</span>

- Smonta un volume:

`diskutil unmountDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/diskX</span>

- Estrai un CD/DVD (smontando prima dell'estrazione):

`diskutil eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk1</span>
