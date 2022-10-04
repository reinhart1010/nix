---
layout: page
title: common/dotnet-ef (polski)
description: "Narzędzia projektowania dla Entity Framework Core."
content_hash: 0b389358cdf3dd29c5fd682e3cefa4d7eda24f8c
related_topics:
  - title: English version
    url: /en/common/dotnet-ef.html
    icon: bi bi-globe
---
# dotnet ef

Narzędzia projektowania dla Entity Framework Core.
Więcej informacji: <https://learn.microsoft.com/ef/core/cli/dotnet>.

- Zaaktualizuj bazę danych do wybranej migracji:

`dotnet ef database update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">migracja</span>

- Wyczyść bazę danych:

`dotnet ef database drop`

- Wyświetl dostępne `DbContext`:

`dotnet ef dbcontext list`

- Wygeneruj kod dla `DbContext` oraz typów encji bazy danych:

`dotnet ef dbcontext scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">connection_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dostawca</span>

- Dodaj nową migrację:

`dotnet ef migrations add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>

- Usuń poprzednią migrację, cofa zmiany w kodzie stworzone dla poprzedniej migracji:

`dotnet ef migrations remove`

- Wyświetl dostępne migracje:

`dotnet ef migrations list`

- Wygeneruj skrypt SQL dla zakresu migracji:

`dotnet ef migrations script `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">początkowa_migracja</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">końcowa_migracja</span>
