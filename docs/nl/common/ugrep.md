---
layout: page
title: common/ugrep (Nederlands)
description: "Ultrasnelle bestandszoeker met interactive UI."
content_hash: b3e1ac9e48c4f3daa9bd73ab96fd7b6de0ab4b01
related_topics:
  - title: Deutsch version
    url: /de/common/ugrep.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ugrep.html
    icon: bi bi-globe
---
# ugrep

Ultrasnelle bestandszoeker met interactive UI.
Meer informatie: <https://github.com/Genivia/ugrep>.

- Open een interactieve TUI om recursief bestanden te zoeken (CTRL-Z voor hulp):

`ugrep --query`

- Zoek recursief met een regex zoekpatroon in de huidige directory naar passende bestanden:

`ugrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Zoek een gegeven bestand of bestanden in een gegeven directory en laat de passende regelnummers zien:

`ugrep --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory</span>

- Zoek recursief in de huidige directory en geef een lijst met passende bestanden:

`ugrep --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Zoek "fuzzy" met maximaal 3 extra, missende of verwisselende karakters in het patroon:

`ugrep --fuzzy=3 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Zoek passende gecomprimeerde bestanden, zip en tar archieven recursief in de huidige directory:

`ugrep --decompress "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Zoek alleen naar bestanden met namen die overeenkomen met een passende `foo*.???` glob patroon:

`ugrep --glob="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo*.???</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Zoek alleen passende bestanden van het type C++ (gebruik `--type=list` voor een lijst van typenamen):

`ugrep --type=cpp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`
