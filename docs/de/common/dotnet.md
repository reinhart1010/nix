---
layout: page
title: common/dotnet (Deutsch)
description: "Plattformübergreifende Kommandozeilenanwendungen für .NET Core."
content_hash: 902d2cf1ec4c580c62bb7dd6235ad50a4bd44e36
related_topics:
  - title: English version
    url: /en/common/dotnet.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dotnet.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dotnet.html
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

Plattformübergreifende Kommandozeilenanwendungen für .NET Core.
Manche Unterbefehle wie `dotnet build` sind separat dokumentiert.
Weitere Informationen: <https://learn.microsoft.com/dotnet/core/tools>.

- Initialisiere ein neues .NET Projekt:

`dotnet new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vorlagen_name</span>

- Stelle nuget-Pakete wieder her:

`dotnet restore`

- Baue des .NET Projekt im aktuellen Ordner und führe es aus:

`dotnet run`

- Führe eine gebaute dotnet-Applikation aus (Benötigt nur die Laufzeitumgebung. Die anderen Befehle benötigen auch den Entwicklungsteil):

`dotnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/anwendung.dll</span>
