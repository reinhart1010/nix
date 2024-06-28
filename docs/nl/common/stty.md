---
layout: page
title: common/stty (Nederlands)
description: "Stel opties in voor een terminalapparaatinterface."
content_hash: 1825ee2105b4ee7f87a49786ac490948e871ca1e
last_modified_at: 2024-06-28
related_topics:
  - title: English version
    url: /en/common/stty.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/stty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/stty.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/stty.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># stty

Stel opties in voor een terminalapparaatinterface.
Meer informatie: <https://www.gnu.org/software/coreutils/stty>.

- Toon alle instellingen voor de huidige terminal:

`stty --all`

- Stel het aantal rijen of kolommen in:

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rows|cols</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal</span>

- Verkrijg de daadwerkelijke overdrachtssnelheid van een apparaat:

`stty --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/apparaat_bestand</span>` speed`

- Reset alle modi naar redelijke waarden voor de huidige terminal:

`stty sane`
