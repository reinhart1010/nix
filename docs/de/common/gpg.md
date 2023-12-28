---
layout: page
title: common/gpg (Deutsch)
description: "GNU Privacy Guard."
content_hash: e03c68bd0c43da03cc74880ce8438616949ea9b3
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/gpg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gpg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gpg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gpg

GNU Privacy Guard.
Siehe `gpg2` für GNU Privacy Guard 2.
Weitere Informationen: <https://gnupg.org>.

- Erstelle einen öffentlichen und privaten GPG Schlüssel interaktiv:

`gpg --full-generate-key`

- Signiere `doc.txt` ohne Verschlüsselung (Ausgabe nach `doc.txt.asc`):

`gpg --clearsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- Verschlüssle und signiere `doc.txt` für alice@beispiel.de und bob@example.org (Ausgabe nach `doc.txt.gpg`):

`gpg --encrypt --sign --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@beispiel.de</span>` --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bob@example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- Verschlüssle `doc.txt` nur mit Passwort (Ausgabe nach `doc.txt.gpg`):

`gpg --symmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- Entschlüssle `doc.txt.gpg` (Ausgabe nach `stdout`):

`gpg --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt.gpg</span>

- Importiere einen öffentlichen Schlüssel:

`gpg --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schlüssel.gpg</span>

- Exportiere den öffentlichen Schlüssel von alice@beispiel.de (Ausgabe nach `stdout`):

`gpg --export --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@beispiel.de</span>

- Exportiere den privaten Schlüssel von alice@beispiel.de (Ausgabe nach `stdout`):

`gpg --export-secret-keys --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@beispiel.de</span>
