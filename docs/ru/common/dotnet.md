---
layout: page
title: common/dotnet (русский)
description: "Кросс-платформенная утилита командной строки .NET для .NET Core."
content_hash: b7a7a55c58f171a79cccec1d50367f0b90295748
last_modified_at: 2023-11-12
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
  - title: polski version
    url: /pl/common/dotnet.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/dotnet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dotnet

Кросс-платформенная утилита командной строки .NET для .NET Core.
Некоторые подкоманды, такие как `dotnet build`, имеют собственную документацию по использованию.
Больше информации: <https://learn.microsoft.com/dotnet/core/tools>.

- Инициализировать новый проект .NET:

`dotnet new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">короткое_имя_шаблона</span>

- Восстановить пакеты nuget:

`dotnet restore`

- Собрать и запустить проект .NET в текущей папке:

`dotnet run`

- Запустить собранное приложение .NET (требуется только среда исполнения, для остальных команд требуется установленный .NET Core SDK):

`dotnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/приложения.dll</span>
