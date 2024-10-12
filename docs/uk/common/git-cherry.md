---
layout: page
title: common/git-cherry (українська)
description: "Виявляє коміти, які ще не були застосовані до першоджерела."
content_hash: 66387c9c3edd4bad4a6b5e197507fb2a5a46cc84
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/git-cherry.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cherry.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-cherry.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-cherry.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cherry.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cherry

Виявляє коміти, які ще не були застосовані до першоджерела.
Більше інформації: <https://git-scm.com/docs/git-cherry>.

- Показує коміти (та їхні повідомлення) із відповідними комітами першоджерела:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>

- Визначає інші першоджерело та тематичну гілку:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>

- Обмежує коміти до тих, що у наданих межах:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base</span>
