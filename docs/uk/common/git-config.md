---
layout: page
title: common/git-config (українська)
description: "Керує спеціальними параметрами конфігурації для репозиторію Git."
content_hash: 8ab31a96cc4997a67ca9dec6fa27dfb8bbd93749
related_topics:
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
  - title: Türkçe version
    url: /tr/common/git-config.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-config.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git config

Керує спеціальними параметрами конфігурації для репозиторію Git.
Конфігурації можуть бути локальні (для поточного репозиторію) або глобальні (для поточного користувача).
Більше інформації: <https://git-scm.com/docs/git-config>.

- Надає перелік лише локальних налаштувань (що зберігаються у `.git/config` поточного репозиторію):

`git config --list --local`

- Надає перелік лише глобальних налаштувань (що зберігаються у `~/.gitconfig`):

`git config --list --global`

- Надає перелік усіх налаштувань незалежно від того, визначені вони локально чи глобально:

`git config --list`

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
