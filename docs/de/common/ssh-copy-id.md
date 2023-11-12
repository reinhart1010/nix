---
layout: page
title: common/ssh-copy-id (Deutsch)
description: "Installiere den öffentlichen Teil eines SSH Schlüssels in der `authorized_keys` Datei auf einem externen Server."
content_hash: 683c69bc97ad048a3bbbc780d5c630a9899a5a66
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-copy-id.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-copy-id

Installiere den öffentlichen Teil eines SSH Schlüssels in der `authorized_keys` Datei auf einem externen Server.
Weitere Informationen: <https://manned.org/ssh-copy-id>.

- Kopiere den eigenen öffentlichen SSH Schlüssels zu einem externen Server:

`ssh-copy-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzer</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">externer_server</span>

- Kopiere den angegebenen öffentlichen SSH Schlüssels zu einem externen Server:

`ssh-copy-id -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/öffentlichem_schlüssel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzer</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">externer_server</span>

- Kopiere den angegeben öffentlichen SSH Schlüssels zu einem externen Server unter Angabe eines bestimmten SSH Ports:

`ssh-copy-id -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/öffentlichem_schlüssel</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzer</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">externer_server</span>
