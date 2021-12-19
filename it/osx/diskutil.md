---
layout: page
title: osx/diskutil (italiano)
description: "Strumento per gestire i dischi locali e i volumi."
content_hash: b215551d23a33e425a45be06a63589b49a7b9c84
related_topics:
  - title: English version
    url: /en/osx/diskutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/diskutil.html
    icon: bi bi-globe
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
