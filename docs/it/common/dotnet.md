---
layout: page
title: common/dotnet (italiano)
description: "Strumenti .NET da linea di comando multipiattaforma per .NET Core."
content_hash: bb1d601458bf3f7aab925c076daacb731b22da5e
related_topics:
  - title: Deutsch version
    url: /de/common/dotnet.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dotnet.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dotnet.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dotnet.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/dotnet.html
    icon: bi bi-globe
---
# dotnet

Strumenti .NET da linea di comando multipiattaforma per .NET Core.
Alcuni comandi aggiuntivi, come `dotnet build`, hanno la propria documentazione.
Maggiori informazioni: <https://learn.microsoft.com/dotnet/core/tools>.

- Inizializza un nuovo progetto .NET:

`dotnet new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_abbreviato_template</span>

- Ripristina pacchetti nuget:

`dotnet restore`

- Costruisci ed esegui il progetto .NET nella directory corrente:

`dotnet run`

- Esegui una applicazione dotnet pacchettizzata (solo il runtime è necessario, il resto dei comandi richiedono .NET Core SDK):

`dotnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/applicazione.dll</span>
