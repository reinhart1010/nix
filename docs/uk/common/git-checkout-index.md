---
layout: page
title: common/git-checkout-index (українська)
description: "Копіює файли з індексу до робочої директорії."
content_hash: 5428e8b7472cbfa9d87f3fd55d640da2345249d0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-checkout-index.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-checkout-index.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git checkout-index

Копіює файли з індексу до робочої директорії.
Більше інформації: <https://git-scm.com/docs/git-checkout-index>.

- Відновлює усі файли, що були видалені з часу останнього коміту:

`git checkout-index --all`

- Відновлює усі файли, що були видалені чи змінені з часу останнього коміту:

`git checkout-index --all --force`

- Відновлює усі файли, що були змінені з часу останнього коміту, ігноруючи файли, що були видалені:

`git checkout-index --all --force --no-create`

- Експортує копію робочої директорії, у стані останнього коміту, до вказаного каталогу (слеш наприкінці обов'язковий):

`git checkout-index --all --force --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/директорії_експорту/</span>
