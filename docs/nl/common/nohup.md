---
layout: page
title: common/nohup (Nederlands)
description: "Laat een proces doorgaan wanneer de terminal wordt beëindigd."
content_hash: a942e32cd90f02ff6c6195c193283e2595077111
last_modified_at: 2024-06-26
related_topics:
  - title: English version
    url: /en/common/nohup.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/nohup.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/nohup.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/nohup.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/nohup.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nohup.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nohup

Laat een proces doorgaan wanneer de terminal wordt beëindigd.
Meer informatie: <https://www.gnu.org/software/coreutils/nohup>.

- Voer een proces uit dat kan doorgaan na het sluiten van de terminal:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Start `nohup` in de achtergrondmodus:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>` &`

- Voer een shell-script uit dat kan doorgaan na het sluiten van de terminal:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.sh</span>` &`

- Voer een proces uit en schrijf de uitvoer naar een specifiek bestand:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand</span>` &`
