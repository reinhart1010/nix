---
layout: page
title: common/ffsend (Deutsch)
description: "Teile Dateien einfach und sicher in der Command-line."
content_hash: 417d325bf2ef8860f79de1fc3c1c45c1bdfeccb0
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/common/ffsend.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ffsend.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ffsend

Teile Dateien einfach und sicher in der Command-line.
Weitere Informationen: <https://gitlab.com/timvisee/ffsend>.

- Lade eine Datei hoch:

`ffsend upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Lade eine Datei herunter:

`ffsend download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Lade eine Datei mit Passwort hoch:

`ffsend upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passwort</span>

- Lade eine passwortgeschützte Datei herunter:

`ffsend download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passwort</span>

- Lade eine Datei hoch und erlaube maximal 4 Downloads:

`ffsend upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--downloads</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>
