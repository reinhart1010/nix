---
layout: page
title: common/curl (Deutsch)
description: "Überträgt Daten von oder zu einem Server."
content_hash: c4d64ac3492f69fb7e3d19d89949f94e77d41598
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/curl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/curl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/curl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/curl.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/curl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/curl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/curl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/curl.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/curl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# curl

Überträgt Daten von oder zu einem Server.
Unterstützt die meisten Protokolle, inklusive HTTP, FTP und POP3.
Weitere Informationen: <https://curl.se/docs/manpage.html>.

- Lade den Inhalt einer URL in eine Datei:

`curl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://beispiel.de</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Lade eine Datei von einer URL herunter:

`curl --remote-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://beispiel.de/datei</span>

- Lade eine Datei herunter, folge Weiterleitungen und setze vergangene Dateitransfers automatisch fort:

`curl --fail --remote-name --location --continue-at - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://beispiel.de/datei</span>

- Sende formular-codierte Daten (POST Anfragen des Typs `application/x-www-form-urlencoded`). Benutze `--data @dateiname` oder `--data @'-'`, um von STDIN zu lesen:

`curl --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'name=karl-dieter'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://beispiel.de/formular</span>

- Sende eine Anfrage mit einem extra Header mit einer eigenen HTTP-Methode:

`curl --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'X-Mein-Header: 123'</span>` --request `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PUT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://beispiel.de</span>

- Sende Daten im JSON-Format und lege den geeigneten Inhaltstyp-Header fest:

`curl --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"name":"karl-dieter"}'</span>` --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Content-Type: application/json'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://beispiel.de/benutzer/1234</span>

- Übergib einen Benutzernamen und frage nach einem Passwort für die Server-Authentifizierung:

`curl --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://beispiel.de</span>

- Übergib Client-Zertifikat und -Schlüssel für eine Ressource und überspringe die Zertifikatsüberprüfung:

`curl --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client.pem</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key.pem</span>` --insecure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://beispiel.de</span>
