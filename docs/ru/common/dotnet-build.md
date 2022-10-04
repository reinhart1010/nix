---
layout: page
title: common/dotnet-build (русский)
description: "Собирает приложение .NET и все его зависимости."
content_hash: da212785429ad89cee827a2a7d1df4169ec9df19
related_topics:
  - title: English version
    url: /en/common/dotnet-build.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dotnet-build.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet-build.html
    icon: bi bi-globe
---
# dotnet build

Собирает приложение .NET и все его зависимости.
Больше информации: <https://learn.microsoft.com/dotnet/core/tools/dotnet-build>.

- Скомпилировать проект или решение в текущей директории:

`dotnet build`

- Скомпилировать проект или решение .NET в режиме debug:

`dotnet build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/проекта_или_решения</span>

- Скомпилировать в режиме release:

`dotnet build --configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Release</span>

- Скомпилировать без восстановления зависимостей:

`dotnet build --no-restore`

- Скомпилировать с заданным уровнем детализации выводимой информации:

`dotnet build --verbosity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet|minimal|normal|detailed|diagnostic</span>

- Скомпилировать для заданной среды исполнения:

`dotnet build --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">идентификатор_среды_исполения</span>

- Указать целевую папку:

`dotnet build --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/папки</span>
