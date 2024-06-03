---
layout: page
title: common/jf (Nederlands)
description: "Werk met JFrog producten zoals Artifactory, Xray, Distribution, Pipelines en Mission Control."
content_hash: 3e844a2c540276f81d7d2e38a008946781a19451
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/jf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jf

Werk met JFrog producten zoals Artifactory, Xray, Distribution, Pipelines en Mission Control.
Meer informatie: <https://jfrog.com/help/r/jfrog-cli/usage>.

- Voeg een nieuwe configuratie toe:

`jf config add`

- Toon de huidige configuratie:

`jf config show`

- Zoek naar artifacts binnen de opgegeven repository en map:

`jf rt search --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repostiory_naam</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad</span>`/`
