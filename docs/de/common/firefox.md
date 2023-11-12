---
layout: page
title: common/firefox (Deutsch)
description: "Ein gratis Open Source Internet Browser."
content_hash: be0154b86d300df57ebeb3feb2a6748cb559f131
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/firefox.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/firefox.html
    icon: bi bi-globe
tldri18n_status: 2
---
# firefox

Ein gratis Open Source Internet Browser.
Weitere Informationen: <https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options>.

- Starte Firefox und öffne eine Website:

`firefox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.duckduckgo.com</span>

- Öffne ein neues Fenster:

`firefox --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.duckduckgo.com</span>

- Öffne ein privates (Inkognito) Fenster:

`firefox --private-window`

- Suche nach "wikipedia" mit der Standard-Suchmaschine:

`firefox --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wikipedia</span>`"`

- Starte Firefox im sicheren Modus (alle Erweiterungen sind deaktiviert):

`firefox --safe-mode`

- Erstelle eine Bildschirmaufnahme einer Website, ohne die GUI zu starten:

`firefox --headless --screenshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/ausgabedatei.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://beispiel.de/</span>

- Verwende ein bestimmtes Profil um mehrere einzelne Instanzen gleichzeitig laufen zu lassen:

`firefox --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://beispiel.de/</span>

- Lege Firefox als Standard-Browser fest:

`firefox --setDefaultBrowser`
