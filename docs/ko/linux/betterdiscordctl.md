---
layout: page
title: linux/betterdiscordctl (한국어)
description: "Linux에서 BetterDiscord 관리."
content_hash: 7b4b3ace2b5e2d123e118f2a6a34bef6fe9fdfc7
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/betterdiscordctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/betterdiscordctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># betterdiscordctl

Linux에서 BetterDiscord 관리.
더 많은 정보: <https://github.com/bb010g/betterdiscordctl#manual>.

- Discord Stable에 BetterDiscord 설치:

`sudo betterdiscordctl install`

- Discord Canary에 BetterDiscord 설치:

`sudo betterdiscordctl --d-flavors canary install`

- Discord PTB에 BetterDiscord 설치:

`sudo betterdiscordctl --d-flavors ptb install`

- Flatpak으로 설치된 Discord에 BetterDiscord 설치:

`sudo betterdiscordctl --d-install flatpak install`

- Snap으로 설치된 Discord에 BetterDiscord 설치:

`sudo betterdiscordctl --d-install snap install`
