---
layout: page
title: common/ssh-keygen (Deutsch)
description: "Generiert ssh Schlüssel für Authentifizierung, Passwort-lose Logins und mehr."
content_hash: 4488ffffbf3fc712965b7c129aa583b0b7a87ba2
related_topics:
  - title: English version
    url: /en/common/ssh-keygen.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-keygen.html
    icon: bi bi-globe
---
# ssh-keygen

Generiert ssh Schlüssel für Authentifizierung, Passwort-lose Logins und mehr.
Weitere Informationen: <https://man.openbsd.org/ssh-keygen>.

- Erstelle ein SSH Schlüssel-Paar interaktiv:

`ssh-keygen`

- Erstelle ein Schlüssel-Paar unter einem bestimmten Dateinamen:

`ssh-keygen -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/datei</span>

- Generiere ein ed25519 Schlüssel-Paar mit 100 Schlüssel-Ableitungs-Iterationen:

`ssh-keygen -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ed25519</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Generiere ein 4096 Bit langen RSA Schlüssel-Paar mit der E-Mail im Kommentarfeld:

`ssh-keygen -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dsa|ecdsa|ed25519|rsa</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -C "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kommentar|e-mail</span>`"`

- Entferne den Schlüssel eines Servers aus der `known_hosts` Datei (hilfreich wenn ein Server seinen Schlüssel aktualisiert hat und der alte somit nicht mehr gilt):

`ssh-keygen -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">externer_server</span>

- Rufe den Fingerabdruck eines Schlüssels im MD5 Hex Format ab:

`ssh-keygen -l -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md5</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/datei</span>

- Ändere das Passwort eines privaten Schlüssels:

`ssh-keygen -p -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/datei</span>

- Ändern Sie den Typ des Schlüsselformats (z. B. vom OPENSSH-Format in PEM), die Datei wird an Ort und Stelle neu geschrieben:

`ssh-keygen -p -N "" -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PEM</span>` -f ~/.ssh/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei</span>
