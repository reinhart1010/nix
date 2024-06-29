---
layout: page
title: linux/zramctl (polski)
description: "Tworzenie i kontrola urządzeń zram."
content_hash: f48b3fc37b50d56d1f7a6cb6dae4ffd057f49cf2
last_modified_at: 2024-06-29
related_topics:
  - title: English version
    url: /en/linux/zramctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/zramctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zramctl

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

`sudo zramctl`
