---
layout: page
title: common/gpg2 (Deutsch)
description: "GNU Privacy Guard 2."
content_hash: 7c28375c4d0444e98ed44457e16da04ff7bf9890
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/gpg2.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gpg2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gpg2

GNU Privacy Guard 2.
Siehe `gpg` für GNU Privacy Guard 1.
Weitere Informationen: <https://docs.releng.linuxfoundation.org/en/latest/gpg.html>.

- Liste alle importierten Schlüssel auf:

`gpg2 --list-keys`

- Verschlüssle eine bestimme Datei für einen bestimmten Empfänger und schreibe den Output in eine neue `.gpg` Datei:

`gpg2 --encrypt --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hans@beispiel.de</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.txt</span>

- Verschlüssle eine bestimmte Datei nur mit einem Passwort und schreibe den Output in eine neue `.gpg` Datei:

`gpg2 --symmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.txt</span>

- Verschlüssle eine bestimmte Datei und schreibe das Ergebnis auf `stdout`:

`gpg2 --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.txt.gpg</span>

- Importiere einen öffentlichen Schlüssel:

`gpg2 --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/öffentlichem_schlüssel.gpg</span>

- Exportiere den öffentlichen Schlüssel einer bestimmten Email-Adresse nach STDOUT:

`gpg2 --export --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hans@beispiel.de</span>

- Exportiere den privaten Schlüssel einer bestimmten Email-Adresse nach STDOUT:

`gpg2 --export-secret-keys --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hans@beispiel.de</span>
