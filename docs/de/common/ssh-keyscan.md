---
layout: page
title: common/ssh-keyscan (Deutsch)
description: "Rufe öffentliche SSH Schlüssel eines externen Servers ab."
content_hash: f290e788f1d57a6a2dbaa1164c3dc678d43de526
related_topics:
  - title: English version
    url: /en/common/ssh-keyscan.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-keyscan.html
    icon: bi bi-globe
---
# ssh-keyscan

Rufe öffentliche SSH Schlüssel eines externen Servers ab.
Weitere Informationen: <https://man.openbsd.org/ssh-keyscan>.

- Rufe alle öffentlichen SSH Schlüssel eines Servers ab:

`ssh-keyscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>

- Rufe alle öffentlichen SSH Schlüssel unter einem bestimmten Port ab:

`ssh-keyscan -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>

- Rufe bestimmte SSH Schüssel-Typen ab:

`ssh-keyscan -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa,dsa,ecdsa,ed25519</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>

- Aktualisiere die `known_hosts` SSH Datei mit dem Fingerabdruck eines bestimmten Servers:

`ssh-keyscan -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` >> ~/.ssh/known_hosts`
