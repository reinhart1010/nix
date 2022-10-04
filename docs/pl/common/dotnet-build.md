---
layout: page
title: common/dotnet-build (polski)
description: "Buduj aplikacje .NET i ich zależności."
content_hash: 2fcec16a8d243a34116e6a4466376dd9a9c17a88
related_topics:
  - title: English version
    url: /en/common/dotnet-build.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dotnet-build.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet-build.html
    icon: bi bi-globe
---
# dotnet build

Buduj aplikacje .NET i ich zależności.
Więcej informacji: <https://learn.microsoft.com/dotnet/core/tools/dotnet-build>.

- Kompiluj projekt lub solucje w bieżącym katalogu:

`dotnet build`

- Kompiluj w konfiguracji debugowania:

`dotnet build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ściezka/do/projektu_lub_solucji</span>

- Kompiluj w konfiguracji wydania:

`dotnet build --configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Release</span>

- Kompiluj bez przywracania zależności:

`dotnet build --no-restore`

- Kompiluj z wybranym poziomem szczegółowości logu:

`dotnet build --verbosity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet|minimal|normal|detailed|diagnostic</span>

- Kompiluj dla wybranego środowiska uruchomieniowego:

`dotnet build --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identyfikator_runtime</span>

- Kompiluj do wybranego katalogu:

`dotnet build --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/katalogu</span>
