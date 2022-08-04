---
layout: page
title: common/git (українська)
description: "Розподілена система контролю версій."
content_hash: e568050ecd72d9fa395e34dd3d160a9a029894d7
related_topics:
  - title: Deutsch version
    url: /de/common/git.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/git.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/common/git.html
    icon: bi bi-globe
---
# git

Розподілена система контролю версій.
Деякі команди, як от `git commit`, мають свою власну документацію.
Більше інформації: <https://git-scm.com/>.

- Перевіряє версію Git:

`git --version`

- Показує базову допомогу:

`git --help`

- Показує допомогу з певної підкоманди Git (наприклад, `commit`, `log` чи іншої):

`git help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">підкоманда</span>

- Виконує підкоманду Git:

`git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">підкоманда</span>

- Виконує підкоманду Git у довільному репозиторії, вказавши шлях до нього:

`git -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/репозиторію</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">підкоманда</span>

- Виконує команду Git із вказаними параметрами:

`git -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config.key</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">значення</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">підкоманда</span>
