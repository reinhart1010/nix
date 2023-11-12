---
layout: page
title: common/dotnet-restore (русский)
description: "Восстанавливает зависимости и утилиты для проекта .NET."
content_hash: a373ccc626b689c87b06a651b52160609f4208b0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dotnet-restore.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dotnet-restore.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet-restore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dotnet restore

Восстанавливает зависимости и утилиты для проекта .NET.
Больше информации: <https://learn.microsoft.com/dotnet/core/tools/dotnet-restore>.

- Восстановить зависимости для проекта или решения .NET в текущей директории:

`dotnet restore`

- Восстановить зависимости для проекта или решенияs .NET по заданному пути:

`dotnet restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/проекта_или_решения</span>

- Восстановить зависимости без кеширования HTTP-запросов:

`dotnet restore --no-cache`

- Принудительно восстановить все зависимости, даже если предыдущее восстановление было успешным:

`dotnet restore --force`

- Восстановить зависимости, считая что ошибки источника пакетов это предупреждения:

`dotnet restore --ignore-failed-sources`

- Восстановить зависимости, используя заданный уровень детализации выводимой информации:

`dotnet restore --verbosity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet|minimal|normal|detailed|diagnostic</span>
