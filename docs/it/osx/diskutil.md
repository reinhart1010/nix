---
layout: page
title: osx/diskutil (italiano)
description: "Strumento per gestire i dischi locali e i volumi."
content_hash: d54e2f52d13a6a0047a0ee9c5c226f30a41a2a41
last_modified_at: 2024-01-31
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
Maggiori informazioni: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- Mostra tutti i dischi correnti, le partizioni e i volumi montati:

`diskutil list`

- Ripara le strutture dati del filesystem di un volume:

`diskutil repairVolume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/diskX</span>

- Smonta un volume:

`diskutil unmountDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/diskX</span>

- Estrai un CD/DVD (smontando prima dell'estrazione):

`diskutil eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk1</span>
