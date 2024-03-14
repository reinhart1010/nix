---
layout: page
title: windows/logoff (italiano)
description: "Termina una sessione di accesso."
content_hash: dd05308ea658c67c95da95cadeb82f2a9f04e5f8
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/windows/logoff.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/logoff.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/logoff.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/logoff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# logoff

Termina una sessione di accesso.
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/logoff>.

- Termina la sessione in uso:

`logoff`

- Termina una sessione con il suo nome o ID:

`logoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_sessione|id_sessione</span>

- Termina la sessione su un server specifico connesso tramite RDP:

`logoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_sessione|id_sessione</span>` /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_server</span>
