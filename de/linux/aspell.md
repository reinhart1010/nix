---
layout: page
title: linux/aspell (Deutsch)
description: "Interaktiver Korrekturleser."
content_hash: 92b132f2ea69d1ea67817b5e70667c8d977436a5
related_topics:
  - title: English version
    url: /en/linux/aspell.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/aspell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/aspell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aspell.html
    icon: bi bi-globe
---
# aspell

Interaktiver Korrekturleser.
Mehr Informationen: <http://aspell.net/>.

- Überprüfe eine einzelne Datei auf Fehler:

`aspell check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/datei</span>

- Liste falsch geschriebene Worte von Standard Input:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` | aspell list`

- Zeige verfügbare Wörterbücher Sprachen:

`aspell dicts`

- Nutze aspell mit einem anderen Wörterbuch (nimmt 2-Buchstaben-Sprachkürzel laut ISO 639 Sprach Code):

`aspell --lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cs</span>

- Zeige alle falsch geschriebenen Wörter von Standard Input und ignoriere alle Wörter in einer persönlichen Wortliste:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` | aspell --personal=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">persönliche-wort-liste.pws</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">list</span>
