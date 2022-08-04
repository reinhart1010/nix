---
layout: page
title: linux/arch-chroot (Deutsch)
description: "Erweiterter `chroot`-Befehl zur Unterstützung des Arch Linux-Installationsprozesses."
content_hash: 8a208b8678413d9f9a9df920984459e03e8fabf5
related_topics:
  - title: English version
    url: /en/linux/arch-chroot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arch-chroot.html
    icon: bi bi-globe
---
# arch-chroot

Erweiterter `chroot`-Befehl zur Unterstützung des Arch Linux-Installationsprozesses.
Weitere Informationen: <https://man.archlinux.org/man/arch-chroot.8>.

- Starte eine interaktive Shell (Standardmäßig `bash`) in einem neuen Root-Verzeichnis:

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/neuem/root</span>

- Spezifiziere den Benutzer (nicht der jetzige Benutzer) der die Shell ausführt:

`arch-chroot -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anderer_benutzer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/neuem/root</span>

- Führe einen benutzerdefinierten Befehl (anstelle des Standardbefehls `bash`) im neuen Root-Verzeichnis aus:

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/neuem/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehlsparameter</span>

- Gib die Shell an, die nicht die Standard-Shell `bash` ist (in diesem Fall sollte das Paket `zsh` auf dem Zielsystem installiert worden sein):

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/neuem/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>
