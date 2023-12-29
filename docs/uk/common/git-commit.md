---
layout: page
title: common/git-commit (українська)
description: "Комітить файли до репозиторію."
content_hash: ca7b217e281ffecd4b64d06dd1f5a4118fcb897b
last_modified_at: 2023-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/git-commit.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-commit.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-commit.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-commit.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-commit.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-commit.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/git-commit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-commit.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-commit.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git commit

Комітить файли до репозиторію.
Більше інформації: <https://git-scm.com/docs/git-commit>.

- Комітить індексовані файли до репозиторію з повідомленням:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">повідомлення</span>`"`

- Комітить індексовані файли з повідомленням, що прочитано у файлі:

`git commit --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_з_повідомленням</span>

- Автоматично індексує усі змінені файли і комітить їх з повідомленням:

`git commit --all --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">повідомлення</span>`"`

- Оновлює останній коміт додаючи до нього щойно індексовані зміни, також змінює геш коміту:

`git commit --amend`

- Комітить тільки певні (вже індексовані) файли:

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу2</span>

- Створює коміт, навіть якщо немає жодного індексованого файлу:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">повідомлення</span>`" --allow-empty`
