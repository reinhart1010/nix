---
layout: page
title: common/ansible-vault (Deutsch)
description: "Verschlüsselt und entschlüsselt Werte, Datenstrukturen und Dateien innerhalb von Ansible-Projekten."
content_hash: c73c26fdee7043f10ddc18c55cb34ea69902f0a3
last_modified_at: 2024-04-19
related_topics:
  - title: English version
    url: /en/common/ansible-vault.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-vault.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-vault

Verschlüsselt und entschlüsselt Werte, Datenstrukturen und Dateien innerhalb von Ansible-Projekten.
Weitere Informationen: <https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>.

- Erstelle eine neue verschlüsselte Vault-Datei mit einer Eingabeaufforderung für ein Passwort:

`ansible-vault create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vault_datei</span>

- Erstelle eine neue verschlüsselte Vault-Datei mit einer Vault-Schlüsseldatei, um sie zu verschlüsseln:

`ansible-vault create --vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schlüsseldatei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vault_datei</span>

- Verschlüssle eine vorhandene Datei mit einer optionalen Schlüsseldatei:

`ansible-vault encrypt --vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schlüsseldatei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vault_file</span>

- Verschlüssle eine Zeichenfolge mit dem verschlüsselten Zeichenfolgenformat von Ansible, wobei interaktive Eingabeaufforderungen angezeigt werden:

`ansible-vault encrypt_string`

- Zeige eine verschlüsselte Datei an, wobei eine Kennwortdatei zum Entschlüsseln verwendet wird:

`ansible-vault view --vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schlüsseldatei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vault_datei</span>

- Verschlüssle eine bereits verschlüsselte Vault Datei mit einer neuen Kennwortdatei neu:

`ansible-vault rekey --vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alte_schlüsseldatei</span>` --new-vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">neue_schlüsseldatei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vault_datei</span>
