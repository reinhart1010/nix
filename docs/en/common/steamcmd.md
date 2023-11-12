---
layout: page
title: common/steamcmd (English)
description: "A command-line version of the Steam client."
content_hash: cfad3a0e42cbb6eb615f07832cbcd1f057830611
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/steamcmd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# steamcmd

A command-line version of the Steam client.
More information: <https://manned.org/steamcmd>.

- Install or update an application anonymously:

`steamcmd +login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anonymous</span>` +app_update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appid</span>` +quit`

- Install or update an application using the specified credentials:

`steamcmd +login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` +app_update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appid</span>` +quit`

- Install an application for a specific platform:

`steamcmd +@sSteamCmdForcePlatformType `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">windows</span>` +login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anonymous</span>` +app_update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appid</span>` validate +quit`
