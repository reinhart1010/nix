---
layout: page
title: linux/pacman-sync (Deutsch)
description: "Arch Linux Paketverwaltungs-Werkzeug."
content_hash: 1e825fe2882fd022677fec4412e7d134370de285
related_topics:
  - title: English version
    url: /en/linux/pacman-sync.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-sync.html
    icon: bi bi-globe
---
# pacman --sync

Arch Linux Paketverwaltungs-Werkzeug.
Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Installiere ein neues Paket:

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Synchronisiere und aktualisiere alle Pakete (füge `--downloadonly` hinzu um die Pakete nur herunterzuladen und nicht zu aktualisieren):

`sudo pacman --sync --refresh --sysupgrade`

- Aktualisiere alle Pakete und installiere ein neues ohne Bestätigungsaufforderung:

`sudo pacman --sync --refresh --sysupgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Suche in der Paketdatenbank mit einem regulärem Ausdruck oder Schlüsselwort:

`pacman --sync --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchmuster</span>`"`

- Zeige Informationen über ein Paket an:

`pacman --sync --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Überschreibe widersprüchliche Dateien während einer Paketaktualisierung:

`sudo pacman --sync --refresh --sysupgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/datei</span>

- Synchronisiere und aktualisiere alle Pakete, ignoriere aber ein bestimmtes Paket (kann mehr als einmal angegeben werden):

`sudo pacman --sync --refresh --sysupgrade --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Entferne nicht installierte Pakete und ungenutzte Repositorys vom Cache (nutze zwei `--clean` Operationen um alle Pakete aufzuräumen):

`sudo pacman --sync --clean`
