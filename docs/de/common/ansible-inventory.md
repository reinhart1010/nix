---
layout: page
title: common/ansible-inventory (Deutsch)
description: "Anzeigen oder Ausgeben eines Ansible-Inventars."
content_hash: 16145072df8bd6d658c0a65b4a2fecafef53237a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ansible-inventory.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible-inventory.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-inventory.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-inventory

Anzeigen oder Ausgeben eines Ansible-Inventars.
Siehe auch: `ansible`.
Weitere Informationen: <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- Anzeigen des Standardinventars:

`ansible-inventory --list`

- Anzeigen eines Benutzerdefinierten Inventars:

`ansbile-inventory --list --inventory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/deiner_datei_oder_deinem_script_oder_deinem_verzeichniss</span>

- Anzeigen des Standardinventars in YAML:

`ansible-inventory --list --yaml`

- Ausgabe des Standardinventars in eine Datei:

`ansible-inventory --list --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>
