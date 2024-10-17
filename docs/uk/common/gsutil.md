---
layout: page
title: common/gsutil (українська)
description: "Доступ до Google Cloud Storage."
content_hash: 1af47f2cfc616cbdb4b869ce2c8694d99fe0fddb
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/gsutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gsutil

Доступ до Google Cloud Storage.
Ви можете використовувати `gsutil` для виконання широкого діапазону завдань із керування контейнерами (buckets) та об’єктами.
Більше інформації: <https://cloud.google.com/storage/docs/gsutil>.

- Вивести всі контейнери (buckets) в проекті, до якого ви ввійшли:

`gsutil ls`

- Вивести об’єкти у контейнері (bucket):

`gsutil ls -r 'gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>`**'`

- Завантажити об'єкт із контейнера (bucket):

`gsutil cp gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ім'я_об'єкта</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/де/зберегти_розташування</span>

- Завантажити об’єкт у контейнер (bucket):

`gsutil cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">місцезнаходження_об'єкта</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_bucket_name</span>`/`

- Перейменувати або перемістіти об’єкти у контейнері (bucket):

`gsutil mv gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">старе_ім'я_об'єкта</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">нове_ім'я_об'єкта</span>

- Створити новий контейнер (bucket) в проекті, у який ви ввійшли:

`gsutil mb gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>

- Видалити контейнер (bucket) та видалити всі об’єкти в ньому:

`gsutil rm -r gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>
