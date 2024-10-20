---
layout: page
title: windows/ipconfig (Nederlands)
description: "Toon en beheer de netwerkconfiguratie van Windows."
content_hash: 5f52240349706920c5878045ca09201254affb08
last_modified_at: 2024-10-20
related_topics:
  - title: Deutsch version
    url: /de/windows/ipconfig.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/ipconfig.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/ipconfig.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/ipconfig.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/ipconfig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/ipconfig.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/ipconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ipconfig

Toon en beheer de netwerkconfiguratie van Windows.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Toon alle netwerkadapters:

`ipconfig`

- Toon een gedetailleerde lijst van netwerkadapters:

`ipconfig /all`

- Vernieuw de IP-adressen voor een netwerkadapter:

`ipconfig /renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adapter</span>

- Laat de IP-adressen voor een netwerkadapter vrij:

`ipconfig /release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adapter</span>

- Toon de lokale DNS-cache:

`ipconfig /displaydns`

- Verwijder alle gegevens uit de lokale DNS-cache:

`ipconfig /flushdns`
