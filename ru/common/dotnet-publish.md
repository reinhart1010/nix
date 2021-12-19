---
layout: page
title: common/dotnet-publish (русский)
description: "Публикует .NET-приложение и его зависимости в папку для развёртываения на целевой системе."
content_hash: c55551e33d583bc375af4526bf0e887195a54b9c
related_topics:
  - title: English version
    url: /en/common/dotnet-publish.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dotnet-publish.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet-publish.html
    icon: bi bi-globe
---
# dotnet publish

Публикует .NET-приложение и его зависимости в папку для развёртываения на целевой системе.
Больше информации: <https://docs.microsoft.com/dotnet/core/tools/dotnet-publish>.

- Скомпилировать проект .NET в режиме release:

`dotnet publish --configuration Release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_проекта</span>

- Опубликовать ваше приложение с заданной средой исполнения .NET Core:

`dotnet publish --self-contained true --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">идентификатор_среды_исполения</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_проекта</span>

- Упаковать приложение в один исполняемый файл для заданной платформы:

`dotnet publish --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">идентификатор_среды_исполения</span>` -p:PublishSingleFile=true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_проекта</span>

- Обрезать неиспользуемые библиотеки чтобы уменьшить размер развёртывания приложения:

`dotnet publish --self-contained true --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">идентификатор_среды_исполения</span>` -p:PublishTrimmed=true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_проекта</span>

- Скомпилировать проект .NET без восстановления зависимостей:

`dotnet publish --no-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_проекта</span>

- Указать целевую папку:

`dotnet publish --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/папки</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_проекта</span>
