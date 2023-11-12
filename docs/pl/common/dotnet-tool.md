---
layout: page
title: common/dotnet-tool (polski)
description: "Zarządzaj narzędziami .NET i szukaj narzędzi opublikowanych w repozytorium NuGet."
content_hash: 1d4b2e35fbc854887dc84dd55855ec1eab2eaeb4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dotnet-tool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dotnet tool

Zarządzaj narzędziami .NET i szukaj narzędzi opublikowanych w repozytorium NuGet.
Więcej informacji: <https://learn.microsoft.com/dotnet/core/tools/global-tools>.

- Zainstaluj narzędzie globalne (nie używaj flagi `--global`, by użyć polecenia dla narzędzi lokalnych):

`dotnet tool install --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dotnetsay</span>

- Zainstaluj narzędzia zdefiniowane w lokalnym manifeście narzędzi:

`dotnet tool restore`

- Zaktualizuj wyspecyfikowane narzędzie globalne (nie używaj flagi `--global`, by użyć polecenia dla narzędzi lokalnych):

`dotnet tool update --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_narzędzia</span>

- Odinstaluj narzędzie globalne (nie używaj flagi `--global`, by użyć polecenia dla narzędzi lokalnych):

`dotnet tool uninstall --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_narzędzia</span>

- Wyświetl zainstalowane narzędzia globalne (nie używaj flagi `--global`, by użyć polecenia dla narzędzi lokalnych):

`dotnet tool list --global`

- Szukaj narzędzi w repozytorium NuGet:

`dotnet tool search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">szukana_fraza</span>

- Wyświetl pomoc:

`dotnet tool --help`
