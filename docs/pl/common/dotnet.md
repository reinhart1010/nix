---
layout: page
title: common/dotnet (polski)
description: "Wieloplatformowe narzędzia wiersza polecenia .NET dla platformy .NET Core."
content_hash: bef5118614823a5e72826668559d047749780ede
last_modified_at: 2024-10-05
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
  - title: italiano version
    url: /it/common/dotnet.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dotnet.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/dotnet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dotnet

Wieloplatformowe narzędzia wiersza polecenia .NET dla platformy .NET Core.
Niektóre podkomendy takie jak `build` mają osobną dokumentację.
Więcej informacji: <https://learn.microsoft.com/dotnet/core/tools>.

- Zainicjuj nowy projekt .NET:

`dotnet new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">krótka_nazwa_szablonu</span>

- Przywróć pakiety NuGet:

`dotnet restore`

- Zbuduj i uruchom projekt .NET w bieżącym katalogu:

`dotnet run`

- Uruchom spakowaną aplikację dotnet (wymaga tylko środowiska wykonawczego, pozostałe polecenia wymagają zainstalowanego zestawu .NET Core SDK):

`dotnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/aplikacji.dll</span>
