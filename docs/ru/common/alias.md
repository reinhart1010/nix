---
layout: page
title: common/alias (русский)
description: "Создает псевдонимы -- слова, которые заменяются командой."
content_hash: 4bee7c7beb0945a4e6c4a9af54de5229351cb9ba
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/alias.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/alias.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/alias.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alias.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/alias.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alias.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/alias.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/alias.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alias.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/alias.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alias.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/alias.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alias.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alias.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/alias.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/alias.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/alias.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/alias.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alias

Создает псевдонимы -- слова, которые заменяются командой.
Срок действия псевдонима истекает с окончанием текущей сессии командной строки, если только не определить его в конфигурационном файле, например: `~/.bashrc`.
Больше информации: <https://tldp.org/LDP/abs/html/aliases.html>.

- Вывести список всех псевдонимов:

`alias`

- Создать типовой псевдоним:

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">псевдоним</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>`"`

- Вывести команду сопоставленную с данным псевдонимом:

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">псевдоним</span>

- Удалить псевдоним:

`unalias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">псевдоним</span>

- Превратить `rm` в интерактивную команду:

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rm</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rm --interactive</span>`"`

- Превратить `la` в ссылку на `ls --all`:

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">la</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls --all</span>`"`
