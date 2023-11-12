---
layout: page
title: common/gcloud (dansk)
description: "Det officielle CLI værktøj for Google Cloud Platform."
content_hash: a5b39402b89875b70d37893405a8ffa4536ee7b0
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/gcloud.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gcloud.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcloud

Det officielle CLI værktøj for Google Cloud Platform.
Mere information: <https://cloud.google.com/sdk/gcloud>.

- List alle aktive konfigurationer:

`gcloud config list`

- Login på en Google account:

`gcloud auth login`

- Sæt et GCP project som standard:

`gcloud config set project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">projekt_navn</span>

- SSH ind til en virtuel maskine:

`gcloud compute ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bruger</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instans</span>

- Vis et overblik af alle Google Compute Engine instanser i et project. Instanser fra alle zoner er listet som standard:

`gcloud compute instances list`

- Opdater en kube-konfiguratonsfil med de korrekte credentials, der peger kubectl mod et spesifikt cluster i Google Kubernetes Engine:

`gcloud container clusters get-credentials `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_navn</span>

- Opdater all gcloud CLI komponenter:

`gcloud components update`

- Vis hjælp for en command:

`gcloud help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kommando</span>
