---
layout: page
title: common/chmod (русский)
description: "Изменить права доступа файлу или папке."
content_hash: 75afda81fb9baed313fcc7d11516ee577f0a521a
related_topics:
  - title: Deutsch version
    url: /de/common/chmod.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chmod.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chmod.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chmod.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chmod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chmod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chmod.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chmod.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/chmod.html
    icon: bi bi-globe
---
# chmod

Изменить права доступа файлу или папке.
Больше информации: <https://www.gnu.org/software/coreutils/chmod>.

- Дать пользователю ([u]ser), который владеет файлом, права на его исполнение (e[x]ecute):

`chmod u+x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл</span>

- Дать права пользователю ([u]ser) права чтения ([r]ead) и записи ([w]rite) в файл/папку:

`chmod u+rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл_или_папка</span>

- Убрать права на исполнение (e[x]ecute) у группы ([g]roup):

`chmod g-x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл</span>

- Дать всем ([a]ll) пользователям права на чтение ([r]ead) и исполнение (e[x]ecute):

`chmod a+rx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл</span>

- Дать другим ([o]thers) (не из группы владельцев файла) такие же права, как и у группы ([g]roup):

`chmod o=g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл</span>

- Убрать все права у других ([o]thers):

`chmod o= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл</span>

- Изменить права рекурсивно, дав группе ([g]roup) и другим ([o]thers) возможность записи ([w]rite) в папку:

`chmod -R g+w,o+w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">папка</span>

- Рекурсивно дать для всех ([a]ll) пользователей права на чтение ([r]ead) файлов и права на исполнение (e[X]ecute) поддиректорий внутри указанной директории:

`chmod -R a+rX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">папка</span>
