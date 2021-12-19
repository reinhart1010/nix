---
layout: page
title: common/git-status (українська)
description: "Показує зміни до файлів у Git-репозиторії."
content_hash: 5eeaa225a429e53ef0fd898c77d7a628d6839582
related_topics:
  - title: Deutsch version
    url: /de/common/git-status.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-status.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-status.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-status.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/git-status.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-status.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-status.html
    icon: bi bi-globe
---
# git status

Показує зміни до файлів у Git-репозиторії.
Списки змінених, доданих та видалених файлів в порівнянні до поточного зареєстрованого коміту.
Більше інформації: <https://git-scm.com/docs/git-status>.

- Показує змінені файли які ще не додані до коміту:

`git status`

- Виводить інформацію у стислому ([s]hort) форматі:

`git status -s`

- Виводить інформацію без неконтрольованих файлів:

`git status --untracked-files=no`

- Виводить інформацію у стислому ([s]hort) форматі разом з інформацією про гілку ([b]ranch):

`git status -sb`
