---
layout: page
title: linux/nixos-rebuild (Deutsch)
description: "Rekonfiguriere eine NixOS-Maschine."
content_hash: 7c74affc40078a01c93894d8d64aecafa955e96e
last_modified_at: 2024-05-06
related_topics:
  - title: English version
    url: /en/linux/nixos-rebuild.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nixos-rebuild

Rekonfiguriere eine NixOS-Maschine.
Weitere Informationen: <https://nixos.org/nixos/manual/#sec-changing-config>.

- Erstelle und wechsle zu einer neuen Konfiguration und nutze diese künftig als Standardkonfiguration:

`sudo nixos-rebuild switch`

- Gib der neu erstellten Standardkonfiguration einen Namen:

`sudo nixos-rebuild switch -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Erstelle und wechsle zu einer neuen Konfiguration, nutze diese künftig als Standardkonfiguration und installiere Updates:

`sudo nixos-rebuild switch --upgrade`

- Setze Änderungen der Konfiguration zurück und wechsle zur vorhergehenden Konfiguration:

`sudo nixos-rebuild switch --rollback`

- Erstelle eine neue Konfiguration und starte diese zukünftig direkt ohne sofort zu wechseln:

`sudo nixos-rebuild boot`

- Erstelle und wechsle direkt zu einer neuen Konfiguration, ändere den Standard-Start-Eintrag nicht (dieses Kommando ist für Testzwecke gedacht):

`sudo nixos-rebuild test`

- Erstelle die Konfiguration und öffne diese in einer virtuellen Maschine:

`sudo nixos-rebuild build-vm`
