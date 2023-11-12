---
layout: page
title: common/fastd (Deutsch)
description: "VPN daemon."
content_hash: e1fdfd8be3df8a58354cc632e021f7769c1cc7db
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/fastd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fastd

VPN daemon.
Arbeitet auf Schicht 2 oder Schicht 3, unterstützt verschiedene Verschlüsselungsmethoden, wird von Freifunk verwendet.
Weitere Informationen: <https://fastd.readthedocs.io/en/stable/>.

- Starte `fastd` mit einer bestimmten Konfigurationsdatei:

`fastd --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/fastd.conf</span>

- Starte einen Schicht-3-VPN mit einer MTU von 1400 und lade den Rest der Konfigurationsparameter aus einer Datei:

`fastd --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tap</span>` --mtu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1400</span>` --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/fastd.conf</span>

- Validiere eine Konfigurationsdatei:

`fastd --verify-config --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/fastd.conf</span>

- Generiere einen neuen Schlüssel:

`fastd --generate-key`

- Zeige den öffentlichen Schlüssel zu einem privaten Schlüssel in einer Konfigurationsdatei an:

`fastd --show-key --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/fastd.conf</span>

- Zeige die aktuelle Version an:

`fastd -v`
