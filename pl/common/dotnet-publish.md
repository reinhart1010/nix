---
layout: page
title: common/dotnet-publish (polski)
description: "Opublikuj aplikację .NET i jej zależności w celu wdrożenia na docelowym systemie."
content_hash: 9328180979b17bff1b739a111f257e49a17336ce
related_topics:
  - title: English version
    url: /en/common/dotnet-publish.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dotnet-publish.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet-publish.html
    icon: bi bi-globe
---
# dotnet publish

Opublikuj aplikację .NET i jej zależności w celu wdrożenia na docelowym systemie.
Więcej informacji: <https://docs.microsoft.com/dotnet/core/tools/dotnet-publish>.

- Opublikuj projekt w konfiguracji wydania:

`dotnet publish --configuration Release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/projektu_lub_solucji</span>

- Opublikuj projekt z dołączonym wybranym środowiskiem uruchomieniowym:

`dotnet publish --self-contained true --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identyfikator_runtime</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/projektu_lub_solucji</span>

- Zapakuj aplikację do pojedyńczego pliku uruchomieniowego dla konkretnej platformy:

`dotnet publish --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identyfikator_runtime</span>` -p:PublishSingleFile=true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/projektu_lub_solucji</span>

- Pomiń nieużywane biblioteki aby obniżyć rozmiar wdrażanej aplikacji:

`dotnet publish --self-contained true --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identyfikator_runtime</span>` -p:PublishTrimmed=true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/projektu_lub_solucji</span>

- Kompiluj projekt bez przywracania zależności:

`dotnet publish --no-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/projektu_lub_solucji</span>

- Wybierz katalog docelowy:

`dotnet publish --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ściezka/do/katalogu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/projektu_lub_solucji</span>
