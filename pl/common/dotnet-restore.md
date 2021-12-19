---
layout: page
title: common/dotnet-restore (polski)
description: "Przywracanie zależności i narzędzi dla projektu .NET."
content_hash: 5ea9fb805ee1aae8f017bb3b6d657b9e5ac45e8d
related_topics:
  - title: English version
    url: /en/common/dotnet-restore.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dotnet-restore.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet-restore.html
    icon: bi bi-globe
---
# dotnet restore

Przywracanie zależności i narzędzi dla projektu .NET.
Więcej informacji: <https://docs.microsoft.com/dotnet/core/tools/dotnet-restore>.

- Przywróć zależności dla projektu lub solucji w bieżącym katalogu:

`dotnet restore`

- Przywróć zależności dla projektu lub solucji w wybranym katalogu:

`dotnet restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/projektu_lub_solucji</span>

- Przywróć zależnośći pomijając cache zapytań HTTP:

`dotnet restore --no-cache`

- Wymuś rozwiązanie wszystkich zależności nawet jeśli poprzednie przywracanie zakończyło się sukcesem:

`dotnet restore --force`

- Ignoruj błędy w trakcie przywracania zależności ze źródeł:

`dotnet restore --ignore-failed-sources`

- Przywróć zależności z wybranym poziomem szczegółowości logów:

`dotnet restore --verbosity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet|minimal|normal|detailed|diagnostic</span>
