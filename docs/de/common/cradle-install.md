---
layout: page
title: common/cradle-install (Deutsch)
description: "Installiere Cradle PHP Framework Komponenten."
content_hash: 464d0b49dd82e22a35523c6061e1a09dbad78112
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cradle-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cradle-install.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cradle-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cradle install

Installiere Cradle PHP Framework Komponenten.
Weitere Informationen: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#install>.

- Installiere Cradle Komponenten mithilfe eines Dialogs:

`cradle install`

- Installiere Cradle Komponenten gewaltsam:

`cradle install --force`

- Überspringe SQL Migrationen:

`cradle install --skip-sql`

- Überspringe Paket-Aktualisierungen:

`cradle install --skip-versioning`

- Zeige Details über eine benutzer-spezifische Datenbank:

`cradle install -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzer</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passwort</span>
