---
layout: page
title: common/ansible-inventory (Deutsch)
description: "Anzeigen oder Ausgeben eines Ansible-Inventars."
content_hash: b06f0408f8b5f53b8b5eca6404288c663a520998
last_modified_at: 2023-12-28
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

`ansible-inventory --list --inventory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/deiner_datei_oder_deinem_script_oder_deinem_verzeichnis</span>

- Anzeigen des Standardinventars in YAML:

`ansible-inventory --list --yaml`

- Ausgabe des Standardinventars in eine Datei:

`ansible-inventory --list --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>
