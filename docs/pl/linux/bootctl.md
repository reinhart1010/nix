---
layout: page
title: linux/bootctl (polski)
description: "Kontroluj ustawienia oprogramowania układowego EFI i zarządzaj programem rozruchowym."
content_hash: 1189dc11b8c5c020363d0fdb7c0752193541a7c0
last_modified_at: 2023-05-02
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bootctl

Kontroluj ustawienia oprogramowania układowego EFI i zarządzaj programem rozruchowym.
Więcej informacji: <https://manned.org/bootctl>.

- Wyświetl informacje o oprogramowaniu układowym i programach rozruchowych:

`bootctl status`

- Wyświetl wszystkie dostępne wpisy programu rozruchowego:

`bootctl list`

- Ustaw opcję, aby uruchomić oprogramowanie układowe przy następnym rozruchu (podobne do `sudo systemctl reboot --firmware-setup`):

`sudo bootctl reboot-to-firmware true`

- Podaj ścieżkę do partycji systemowej EFI (domyślnie `/efi/`, `/boot/` lub `/boot/efi`):

`bootctl --esp-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ścieżka/do/partycji_systemowej_efi/</span>

- Zainstaluj `systemd-boot` do partycji systemowej EFI:

`sudo bootctl install`

- Usuń wszystkie zainstalowane wersje `systemd-boot` z partycji systemowej EFI:

`sudo bootctl remove`
