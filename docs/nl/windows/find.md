---
layout: page
title: windows/find (Nederlands)
description: "Vind een gespecificieerde string in een bestand."
content_hash: 80e0dbb91b15d503529a9aa319cfa85427479212
related_topics:
  - title: English version
    url: /en/windows/find.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/find.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/find.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/find.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/find.html
    icon: bi bi-globe
---
# find

Vind een gespecificieerde string in een bestand.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/find>.

- Vind de lijnen dat een specifieke string bevatten:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory</span>

- Laat lijnen zie die de string niet bevatten:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory</span>` /v`

- Toon het aantal lijnen dat de string bevat:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory</span>` /c`

- Laat het aantal lijnen zien samen met de lijnen:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory</span>` /n`
