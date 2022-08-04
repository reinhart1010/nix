---
layout: page
title: common/age (Deutsch)
description: "Ein einfaches, modernes und sicheres Dateiverschlüsselungswerkzeug."
content_hash: 5ab4bfd7dde7b17f00214542e43195e9a15d7749
related_topics:
  - title: English version
    url: /en/common/age.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/age.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/age.html
    icon: bi bi-globe
---
# age

Ein einfaches, modernes und sicheres Dateiverschlüsselungswerkzeug.
Weitere Informationen: <https://age-encryption.org>.

- Generiere eine verschlüsselte Datei, die mit einer Passphrase entschlüsselt werden kann:

`age --passphrase --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verschlüsselter_datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/unverschlüsselter_datei</span>

- Generiere ein Schlüsselpaar, speichere dabei den privaten Schlüssel in einer unverschlüsselten Datei und gib den öffentlichen Schlüssel zu stdout aus:

`age-keygen --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Verschlüssle eine Datei mit einem oder mehr öffentlichen Schlüsseln, die als Zeichenketten eingegeben werden:

`age --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">öffentlicher_schlüssel_1</span>` --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">öffentlicher_schlüssel_2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/unverschlüsselter_datei</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verschlüsselter_datei</span>

- Verschlüssle eine Datei mit einem oder mehr öffentlichen Schlüsseln, die in einer Empfängerdatei angegeben sind:

`age --recipients-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/empfängerdatei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/unverschlüsselter_datei</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verschlüsselter_datei</span>

- Entschlüssle eine Datei mit einer Passphrase:

`age --decrypt --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/entschlüsselter_datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verschlüsselter_datei</span>

- Entschlüssle eine Datei mit einer privaten Schlüsseldatei:

`age --decrypt --identity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/privater_schlüsseldatei</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/entschlüsselter_datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verschlüsselter_datei</span>
