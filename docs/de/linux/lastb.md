---
layout: page
title: linux/lastb (Deutsch)
description: "Zeigt eine Liste der zuletzt angemeldeten Benutzer an."
content_hash: c0b25de32abb6dc225714690370af1c0cfb6e02a
related_topics:
  - title: English version
    url: /en/linux/lastb.html
    icon: bi bi-globe
---
# lastb

Zeigt eine Liste der zuletzt angemeldeten Benutzer an.
Weitere Informationen: <https://manned.org/lastb>.

- Zeige eine Liste aller zuletzt angemeldeten Benutzer an:

`sudo lastb`

- Zeige eine Liste aller zuletzt angemeldeten Benutzer seit einem bestimmten Zeitpunkt an:

`sudo lastb --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>

- Zeige eine Liste aller zuletzt angemeldeten Benutzer bis zu einem bestimmten Zeitpunkt an:

`sudo lastb --until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>

- Zeige eine Liste aller angemeldeten Benutzer zu einem bestimmten Zeitpunkt an:

`sudo lastb --present `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>

- Zeige eine Liste aller zuletzt angemeldeten Benutzer und übersetze die IP zu einem Hostnamen:

`sudo lastb --dns`
