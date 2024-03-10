---
layout: page
title: linux/arch-chroot (Deutsch)
description: "Erweiterter `chroot`-Befehl zur Unterstützung des Arch-Linux-Installationsprozesses."
content_hash: 477d804ea4ef802a511656ac632b42975ec7d86b
last_modified_at: 2024-03-10
related_topics:
  - title: English version
    url: /en/linux/arch-chroot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arch-chroot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arch-chroot

Erweiterter `chroot`-Befehl zur Unterstützung des Arch-Linux-Installationsprozesses.
Weitere Informationen: <https://man.archlinux.org/man/arch-chroot.8>.

- Starte eine interaktive Shell (Standardmäßig Bash) in einem neuen Root-Verzeichnis:

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/neuem/root</span>

- Spezifiziere den Benutzer (nicht der jetzige Benutzer) der die Shell ausführt:

`arch-chroot -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anderer_benutzer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/neuem/root</span>

- Führe einen benutzerdefinierten Befehl (anstelle des Standardbefehls Bash) im neuen Root-Verzeichnis aus:

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/neuem/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehlsparameter</span>

- Gib die Shell an, die nicht die Standard-Shell Bash ist (in diesem Fall sollte das Paket `zsh` auf dem Zielsystem installiert worden sein):

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/neuem/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>
