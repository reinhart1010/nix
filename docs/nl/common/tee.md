---
layout: page
title: common/tee (Nederlands)
description: "Lees van `stdin` en schrijf naar `stdout` en bestanden (of commando's)."
content_hash: 231db4bcd4bec2ec68e07be3fe84715c19899319
last_modified_at: 2024-06-28
related_topics:
  - title: English version
    url: /en/common/tee.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tee.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tee.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tee

Lees van `stdin` en schrijf naar `stdout` en bestanden (of commando's).
Meer informatie: <https://www.gnu.org/software/coreutils/tee>.

- Kopieer `stdin` naar elk bestand en ook naar `stdout`:

`echo "voorbeeld" | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Voeg toe aan de opgegeven bestanden, overschrijf niet:

`echo "voorbeeld" | tee -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon `stdin` naar de terminal en leid het ook door naar een ander programma voor verdere verwerking:

`echo "voorbeeld" | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xargs printf "[%s]"</span>

- Maak een directory genaamd "voorbeeld", tel het aantal tekens in "voorbeeld" en schrijf "voorbeeld" naar de terminal:

`echo "voorbeeld" | tee >(xargs mkdir) >(wc -c)`
