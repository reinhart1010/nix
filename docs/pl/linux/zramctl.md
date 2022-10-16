---
layout: page
title: linux/zramctl (polski)
description: "Tworzenie i kontrola urządzeń zram."
content_hash: 16d013a4363a9f6af2ed028ca44506b1d665cafb
related_topics:
  - title: English version
    url: /en/linux/zramctl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># zramctl

Tworzenie i kontrola urządzeń zram.
Użyj `mkfs` lub `mkswap` aby sformatować urządzenia zram na partycje.
Więcej informacji: <https://manned.org/zramctl>.

- Sprawdzenie, czy zram jest włączony:

`lsmod | grep -i zram`

- Włączenie zram z dynamiczną liczbą urządzeń (użyj `zramctl` aby skonfigurować urządzenia dalej):

`sudo modprobe zram`

- Włączenie zram z dokładnie 2 urządzeniami:

`sudo modprobe zram num_devices=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Znalezienie i inicjalizacja następnego wolnego urządzenia zram jako 2 GB napęd wirtualny z użyciem kompresji LZ4:

`sudo zramctl --find --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2GB</span>` --algorithm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lz4</span>

- Wyświetlenie aktualnie zainicjalizowanych urządzeń:

`zramctl`
