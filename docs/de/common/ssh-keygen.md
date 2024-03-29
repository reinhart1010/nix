---
layout: page
title: common/ssh-keygen (Deutsch)
description: "Generiert SSH Schlüssel für Authentifizierung, Passwort-lose Logins und mehr."
content_hash: eaf3867cf3916afc0cedcd33fac85acfbd5e7ad8
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/ssh-keygen.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-keygen.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-keygen.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ssh-keygen

Generiert SSH Schlüssel für Authentifizierung, Passwort-lose Logins und mehr.
Weitere Informationen: <https://man.openbsd.org/ssh-keygen>.

- Erstelle ein SSH Schlüssel-Paar interaktiv:

`ssh-keygen`

- Generiere ein ed25519 Schlüssel-Paar mit 32 Schlüssel-Ableitungs-Iterationen und speicher unter einem bestimmten Dateinamen:

`ssh-keygen -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ed25519</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">32</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/datei</span>

- Generiere ein 4096 Bit langen RSA Schlüssel-Paar mit der E-Mail im Kommentarfeld:

`ssh-keygen -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -C "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kommentar|e-mail</span>`"`

- Entferne den Schlüssel eines Servers aus der `known_hosts` Datei (hilfreich wenn ein Server seinen Schlüssel aktualisiert hat und der alte somit nicht mehr gilt):

`ssh-keygen -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">externer_server</span>

- Rufe den Fingerabdruck eines Schlüssels im MD5 Hex Format ab:

`ssh-keygen -l -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md5</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/datei</span>

- Ändere das Passwort eines privaten Schlüssels:

`ssh-keygen -p -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/datei</span>

- Ändern Sie den Typ des Schlüsselformats (z. B. vom OPENSSH-Format in PEM), die Datei wird an Ort und Stelle neu geschrieben:

`ssh-keygen -p -N "" -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PEM</span>` -f ~/.ssh/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>
