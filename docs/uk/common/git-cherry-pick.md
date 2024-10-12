---
layout: page
title: common/git-cherry-pick (українська)
description: "Застосовує зміни, зроблені у наявних комітах, до поточної гілки."
content_hash: 22f3b92ccc1d706532e8145e4050a471416d058a
last_modified_at: 2024-10-12
related_topics:
  - title: বাংলা version
    url: /bn/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cherry-pick.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cherry-pick

Застосовує зміни, зроблені у наявних комітах, до поточної гілки.
Для застосування змін до іншої гілки спершу виконайте `git checkout`, аби переключитися на бажану гілку.
Більше інформації: <https://git-scm.com/docs/git-cherry-pick>.

- Застосовує коміт до поточної гілки:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">коміт</span>

- Застосовує проміжок комітів до поточної гілки (дивіться також `git rebase --onto`):

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">початковий_коміт</span>`~..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">кінцевий_коміт</span>

- Застосовує декілька (непослідовних) комітів до поточної гілки:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">коміт1 коміт2 ...</span>

- Додає зміни з коміту до робочої директорії без створення коміту:

`git cherry-pick --no-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">коміт</span>
