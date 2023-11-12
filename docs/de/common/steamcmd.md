---
layout: page
title: common/steamcmd (Deutsch)
description: "Ein Kommandozeilenwerkzeug, um über Steam verfügbare Anwendungen zu verwalten."
content_hash: 1c991fcf0fc4ebbdc47d5f064413d6d3887c245b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/steamcmd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# steamcmd

Ein Kommandozeilenwerkzeug, um über Steam verfügbare Anwendungen zu verwalten.
Weitere Informationen: <https://manned.org/steamcmd>.

- Installiere und aktualisiere eine Anwendung ohne dich einzuloggen:

`steamcmd +login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anonymous</span>` +app_update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anwendungs_id</span>` +quit`

- Installiere oder aktualisiere eine Anwendung unter Angabe deiner Zugangsdaten:

`steamcmd +login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>` +app_update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anwendungs_id</span>` +quit`

- Installiere eine Anwendung für eine bestimmte Plattform:

`steamcmd +@sSteamCmdForcePlatformType `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">windows</span>` +login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>` +app_update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anwendungs_id</span>` validate +quit`
