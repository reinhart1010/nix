---
layout: page
title: common/gcloud-auth (українська)
description: "Видача та скасування авторизації для `gcloud` і керування обліковими даними."
content_hash: 864588d0ed576e1d7938ae87a71cab6d47643db2
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/gcloud-auth.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gcloud-auth.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcloud-auth.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcloud auth

Видача та скасування авторизації для `gcloud` і керування обліковими даними.
Дивіться також: `gcloud`.
Більше інформації: <https://cloud.google.com/sdk/gcloud/reference/auth>.

- Авторизувати доступ до Google Cloud для `gcloud` CLI за допомогою облікових даних користувача Google Cloud і встановити поточний обліковий запис як активний:

`gcloud auth login`

- Авторизувати доступ до Google Cloud, подібно до `gcloud auth login`, але за допомогою облікових даних сервісного облікового запису:

`gcloud auth activate-service-account`

- Керувати Application Default Credentials (ADC) для хмарних клієнтських бібліотек:

`gcloud auth application-default`

- Вивести список облікових записів Google Cloud, які зараз автентифіковані у вашій системі:

`gcloud auth list`

- Вивести токен (token) доступу поточного облікового запису:

`gcloud auth print-access-token`

- Видалити облікові дані доступу до облікового запису:

`gcloud auth revoke`
