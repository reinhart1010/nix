---
layout: page
title: common/gcloud (Deutsch)
description: "Das offizielle CLI-Tool für die Google Cloud Platform."
content_hash: 9859c73e66aff0246b0011db63350a47b6f55249
last_modified_at: 2023-10-14
related_topics:
  - title: dansk version
    url: /da/common/gcloud.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gcloud.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gcloud

Das offizielle CLI-Tool für die Google Cloud Platform.
Weitere Informationen: https://cloud.google.com/sdk/gcloud.

- Liste alle Eigenschaften der aktiven Konfiguration auf:

`gcloud config list`

- Mit einem Google-Konto anmelden:

`gcloud auth login`

- Lege das aktive Projekt fest:

`gcloud config set project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Projektname</span>

- Stelle eine SSH-Verbindung zu einer virtuellen Maschineninstanz her:

`gcloud compute ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Benutzer</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Instanz</span>

- Zeige alle Google Compute Engine-Instanzen in einem Projekt an. Standardmäßig werden Instanzen aus allen Zonen aufgelistet:

`gcloud compute instances list`

- Aktualisiere eine kubeconfig-Datei mit den entsprechenden Anmeldeinformationen, um kubectl auf einen bestimmten Cluster in Google Kubernetes Engine auszurichten:

`gcloud container clusters get-credentials `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Clustername</span>

- Aktualisiere alle gcloud CLI-Komponenten:

`gcloud components update`

- Zeige Hilfe für einen bestimmten Befehl an:

`gcloud help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Befehl</span>
