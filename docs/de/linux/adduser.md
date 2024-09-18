---
layout: page
title: linux/adduser (Deutsch)
description: "Tool um Benutzer hinzuzufügen."
content_hash: 1ba9dcbd3681952d0af226246109599e27c17af5
last_modified_at: 2024-09-18
related_topics:
  - title: English version
    url: /en/linux/adduser.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/adduser.html
    icon: bi bi-globe
  - title: suomi version
    url: /fi/linux/adduser.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/adduser.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/adduser.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/adduser.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/adduser.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/adduser.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/adduser.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/adduser.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adduser

Tool um Benutzer hinzuzufügen.
Weitere Informationen: <https://manned.org/adduser>.

- Erstelle einen neuen Benutzer mit einem Standard-Home-Verzeichnis und Aufforderung an den Benutzer, ein Passwort festzulegen:

`adduser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>

- Erstelle einen neuen Benutzer ohne Home-Verzeichnis:

`adduser --no-create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>

- Erstelle einen neuen Benutzer mit einem Home-Verzeichnis unter dem angegebenen Pfad:

`adduser --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/home</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>

- Erstelle einen neuen Benutzer, bei dem die angegebene Shell als Anmeldeshell eingestellt ist:

`adduser --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>

- Erstelle einen neuen Benutzer und füge ihn zur angegebenen Gruppe hinzu:

`adduser --ingroup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>
