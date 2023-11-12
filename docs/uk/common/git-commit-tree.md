---
layout: page
title: common/git-commit-tree (українська)
description: "Низькорівнева утиліта для створення об'єктів комітів."
content_hash: 37f41b78216aa193753623245f1e25806514de80
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-commit-tree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit-tree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git commit-tree

Низькорівнева утиліта для створення об'єктів комітів.
Дивись також: `git commit`.
Більше інформації: <https://git-scm.com/docs/git-commit-tree>.

- Створює об'єкт коміту із певним повідомленням:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">повідомлення</span>`"`

- Створює об'єкт коміту читаючи повідомлення з файлу (використовуй `-` для читання зі стандартного введення):

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Створює GPG-підписаний об'єкт коміту:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">повідомлення</span>`" --gpg-sign`

- Створює об'єкт коміту із певним батьківським об'єктом коміту:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">повідомлення</span>`" -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha_батьківського_коміту</span>
