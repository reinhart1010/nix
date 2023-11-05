---
layout: page
title: linux/pkgctl-repo (Nederlands)
description: "Beheer Git verpakkingsrepositories en hun configuratie voor Arch Linux."
content_hash: 2628061e7bc06dff98dd7e87164f52ea96c4d1b7
last_modified_at: 2023-11-05
related_topics:
  - title: English version
    url: /en/linux/pkgctl-repo.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pkgctl repo

Beheer Git verpakkingsrepositories en hun configuratie voor Arch Linux.
Bekijk ook: `pkgctl`.
Meer informatie: <https://man.archlinux.org/man/pkgctl-repo.1>.

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
