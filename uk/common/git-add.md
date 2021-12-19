---
layout: page
title: common/git-add (українська)
description: "Додає змінені файли до індексу."
content_hash: af22354155b9a7419afa0c3f7eb3efbeceaa5b05
related_topics:
  - title: Deutsch version
    url: /de/common/git-add.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-add.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-add.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-add.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-add.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-add.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-add.html
    icon: bi bi-globe
---
# git add

Додає змінені файли до індексу.
Більше інформації: <https://git-scm.com/docs/git-add>.

- Додає змінені файли до індексу:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Додає усі файли (контрольовані та неконтрольовані):

`git add -A`

- Додає тільки ті файли, що вже контрольовані:

`git add -u`

- Додає й ті файли, що ігноруються:

`git add -f`

- Інтерактивно індексує частини файлів:

`git add -p`

- Інтерактивно індексує частини вказаного файлу:

`git add -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Інтерактивно індексує файл:

`git add -i`
