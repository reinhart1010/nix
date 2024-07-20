---
layout: page
title: linux/eselect-repository (Nederlands)
description: "Een `eselect`-module voor het configureren van ebuild-repositories voor Portage."
content_hash: 0f9c788d44cfe66b87d31778c4f4678d79c200bc
last_modified_at: 2024-07-20
related_topics:
  - title: English version
    url: /en/linux/eselect-repository.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/eselect-repository.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eselect repository

Een `eselect`-module voor het configureren van ebuild-repositories voor Portage.
Na het inschakelen van een repository moet je `emerge --sync repo_name` uitvoeren om ebuilds te downloaden.
Meer informatie: <https://wiki.gentoo.org/wiki/Eselect/Repository>.

- Toon alle ebuild-repositories geregistreerd op <https://repos.gentoo.org>:

`eselect repository list`

- Toon ingeschakelde repositories:

`eselect repository list -i`

- Schakel een repository uit de lijst in op naam of index van de `list`-opdracht:

`eselect repository enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam|index</span>

- Schakel een niet-geregistreerde repository in:

`eselect repository add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsync|git|mercurial|svn|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sync_uri</span>

- Schakel repositories uit zonder hun inhoud te verwijderen:

`eselect repository disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo1 repo2 ...</span>

- Schakel repositories uit en verwijder hun inhoud:

`eselect repository remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo1 repo2 ...</span>

- Maak een lokale repository aan en schakel deze in:

`eselect repository create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/repo</span>
