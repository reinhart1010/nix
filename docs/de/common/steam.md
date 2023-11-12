---
layout: page
title: common/steam (Deutsch)
description: "Eine Plattform für Videospiele von Valve."
content_hash: 1edbbe297928aca22fde58ede43af3baf747c2dc
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/steam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# steam

Eine Plattform für Videospiele von Valve.
Weitere Informationen: <https://developer.valvesoftware.com/wiki/Command_Line_Options>.

- Starte Steam und gebe Debug-Nachrichten auf die Standardausgabe aus:

`steam`

- Starte Steam und aktiviere die eingebaute Debug-Menüoption:

`steam -console`

- Aktiviere die Menüoption für die Steam-Konsole und öffne diese in einer aktiven Steam-Instanz:

`steam steam://open/console`

- Logge dich in Steam mit den angegebenen Zugangsdaten ein:

`steam -login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passwort</span>

- Starte Steam im Big-Picture-Modus:

`steam -tenfoot`

- Stoppe Steam:

`steam -shutdown`
