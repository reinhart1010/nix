---
layout: page
title: common/rg (Nederlands)
description: "Ripgrep is een recursieve regel-georiënteerde zoek tool."
content_hash: a7932564899252695208d8aab754f0bea4428de4
last_modified_at: 2023-12-22
related_topics:
  - title: English version
    url: /en/common/rg.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/rg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rg

Ripgrep is een recursieve regel-georiënteerde zoek tool.
Wil een sneller alternatief zijn dan `grep`.
Meer informatie: <https://github.com/BurntSushi/ripgrep>.

- Zoek recursief in de huidige map naar een reguliere expressie:

`rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>

- Zoek recursief in de huidige map naar een reguliere expressie, inclusief verborgen bestanden en bestanden opgenomen in `.gitignore`:

`rg --no-ignore --hidden `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>

- Zoek alleen in een subset van mappen naar een reguliere expressie:

`rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set_van_submappen</span>

- Zoek in bestanden die overeenkomen met een glob (bijv. `README.*`) naar een reguliere expressie:

`rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>` --glob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">glob</span>

- Zoek naar bestandsnamen die overeenkomen met een reguliere expressie:

`rg --files | rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>

- Toon alleen overeenkomende bestanden (handig bij het doorsturen naar andere commando's):

`rg --files-with-matches `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>

- Toon regels die niet overeenkomen met de gegeven reguliere expressie:

`rg --invert-match `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>

- Zoek naar een letterlijk string pattroon:

`rg --fixed-strings -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>
