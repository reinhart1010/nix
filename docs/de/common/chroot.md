---
layout: page
title: common/chroot (Deutsch)
description: "Führe einen Befehl oder eine interaktive Shell mit einem speziellen root-Verzeichnis aus."
content_hash: d8762769463fdb1d8abc099e62d42318d4240959
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/common/chroot.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chroot.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chroot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chroot.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chroot.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/chroot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chroot

Führe einen Befehl oder eine interaktive Shell mit einem speziellen root-Verzeichnis aus.
Weitere Informationen: <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- Führe einen Befehl mit einem neuen root-Verzeichnis aus:

`chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/root_verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>

- Lege einen Benutzer und eine Gruppe (ID oder Name) fest, der benutzt werden soll:

`chroot --userspec=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzer:gruppe</span>
