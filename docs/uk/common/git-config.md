---
layout: page
title: common/git-config (українська)
description: "Керує спеціальними параметрами конфігурації для репозиторію Git."
content_hash: eb1e3cb6052d34f8dc13c24a3e5e111ec73d3137
last_modified_at: 2023-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/git-config.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-config.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-config.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-config.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-config.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-config.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-config.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git config

Керує спеціальними параметрами конфігурації для репозиторію Git.
Конфігурації можуть бути локальні (для поточного репозиторію) або глобальні (для поточного користувача).
Більше інформації: <https://git-scm.com/docs/git-config>.

- Надає перелік лише локальних налаштувань (що зберігаються у `.git/config` поточного репозиторію):

`git config --list --local`

- Надає перелік лише глобальних налаштувань (що зберігаються у `~/.gitconfig`):

`git config --list --global`

- Отримує значення для наданого параметру конфігурації:

`git config alias.unstage`

- Встановлює глобальне значення для наданого параметру конфігурації:

`git config --global alias.unstage "reset HEAD --"`

- Повертає значення по замовчанню для наданого глобального параметру конфігурації:

`git config --global --unset alias.unstage`

- Відкриває для редагування файл конфігурацій поточного репозиторію у редакторі по замовчуванню:

`git config --edit`

- Відкриває для редагування файл з глобальними конфігураціями у редакторі по замовчанню:

`git config --global --edit`
