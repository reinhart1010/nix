---
layout: page
title: common/fdroid (Deutsch)
description: "F-Droid Build Tool."
content_hash: 125897d7d8bcbf02e72855aa1127dfc48f7a731f
related_topics:
  - title: English version
    url: /en/common/fdroid.html
    icon: bi bi-globe
---
# fdroid

F-Droid Build Tool.
F-Droid ist ein installierbarer Katalog mit FOSS (Freie Open Source Software) Apps für Android.
Weitere Informationen: <https://f-droid.org/>.

- Kompiliere eine bestimmte App:

`fdroid build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Kompiliere eine bestimmte App in einer Build-Server-VM:

`fdroid build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>` --server`

- Veröffentliche die App im lokalen Repository:

`fdroid publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Installiere die App auf jedem verbundenen Gerät:

`fdroid install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Überprüfe, ob die Metadaten korrekt formatiert sind:

`fdroid lint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Korrigiere die Formatierung automatisch (wenn möglich):

`fdroid rewritemeta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>
