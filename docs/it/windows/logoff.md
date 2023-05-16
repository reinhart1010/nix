---
layout: page
title: windows/logoff (italiano)
description: "Termina una sessione di accesso."
content_hash: 318eeedd3d769a1047055c6679bdff4022c378ce
last_modified_at: 2023-05-09
related_topics:
  - title: English version
    url: /en/windows/logoff.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/logoff.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/logoff.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># logoff

Termina una sessione di accesso.
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/logoff>.

- Termina la sessione in uso:

`logoff`

- Termina una sessione con il suo nome o id:

`logoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_sessione|id_sessione</span>

- Termina la sessione su un server specifico connesso tramite RDP:

`logoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_sessione|id_sessione</span>` /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_server</span>