---
layout: page
title: linux/pkgctl-repo (Nederlands)
description: "Beheer Git verpakkingsrepositories en hun configuratie voor Arch Linux."
content_hash: 216a59a99a3e04f6e39b5924d09fe5fa5d8858f1
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/linux/pkgctl-repo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkgctl repo

Beheer Git verpakkingsrepositories en hun configuratie voor Arch Linux.
Bekijk ook: `pkgctl`.
Meer informatie: <https://manned.org/pkgctl-repo.1>.

- Kloon een pakketrepository (vereist het instellen van een SSH-key in uw Arch Linux GitLab-account):

`pkgctl repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkgname</span>

- Kloon een pakketrepository via HTTPS:

`pkgctl repo clone --protocol=https `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkgname</span>

- Maak een nieuwe GitLab pakketrepository en kloon het na het aanmaken (vereist valide GitLab API authenticatie):

`pkgctl repo create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkgbase</span>

- Wissel een pakketrepository naar een specifieke versie:

`pkgctl repo switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versie</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkgbase</span>

- Open een pakketrepository's website:

`pkgctl repo web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkgbase</span>
