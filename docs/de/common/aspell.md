---
layout: page
title: common/aspell (Deutsch)
description: "Interaktiver Korrekturleser."
content_hash: de1b5cddd4b2e0dce97e78a5ad449b6357460c21
last_modified_at: 2024-08-13
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aspell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aspell

Interaktiver Korrekturleser.
Weitere Informationen: <http://aspell.net/>.

- Überprüfe eine einzelne Datei auf Fehler:

`aspell check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/datei</span>

- Liste falsch geschriebene Worte von Standard Input:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` | aspell list`

- Zeige verfügbare Wörterbuchsprachen:

`aspell dicts`

- Nutze `aspell` mit einem anderen Wörterbuch (nimmt 2-Zeichen-Locale laut ISO 639 Sprach Code):

`aspell --lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cs</span>

- Zeige alle falsch geschriebenen Wörter von Standard Input und ignoriere alle Wörter in einer persönlichen Wortliste:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` | aspell --personal=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">persönliche-wort-liste.pws</span>` list`
