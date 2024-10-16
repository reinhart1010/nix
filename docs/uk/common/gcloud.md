---
layout: page
title: common/gcloud (українська)
description: "Офіційний CLI інструмент для Google Cloud Platform."
content_hash: 079b0fc4ccb18c35d50a332f5074a39ac84cadf9
last_modified_at: 2024-10-16
related_topics:
  - title: dansk version
    url: /da/common/gcloud.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/gcloud.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gcloud.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/gcloud.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gcloud.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcloud.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcloud

Офіційний CLI інструмент для Google Cloud Platform.
Примітка: підкоманди `gcloud` мають власну документацію щодо використання.
Більше інформації: <https://cloud.google.com/sdk/gcloud>.

- Вивести всі властивості в активній конфігурації:

`gcloud config list`

- Увійти в обліковий запис Google:

`gcloud auth login`

- Встановити активний проект:

`gcloud config set project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_проекту</span>

- SSH в екземпляр віртуальної машини:

`gcloud compute ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">користувач</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">екземпляр</span>

- Вивести всі екземпляри Google Compute Engine у проекті (за замовчуванням виводяться екземпляри з усіх зон):

`gcloud compute instances list`

- Оновити файл kubeconfig відповідними обліковими даними, щоб вказати `kubectl` на певний кластер у Google Kubernetes Engine (GKE):

`gcloud container clusters get-credentials `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_кластера</span>

- Оновити усі компоненти `gcloud`:

`gcloud components update`

- Вивести довідки для заданої команди:

`gcloud help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>
