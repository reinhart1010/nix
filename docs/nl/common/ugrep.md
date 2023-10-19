---
layout: page
title: common/ugrep (Nederlands)
description: "Ultrasnelle bestandszoeker met interactive UI."
content_hash: 5733c07472df8ace67ee5245ea786f7280e5bd4d
last_modified_at: 2023-10-19
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

- Zoek recursief met een regex zoekpatroon in de huidige map naar passende bestanden:

`ugrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Zoek een gegeven bestand of bestanden in een gegeven map en laat de passende regelnummers zien:

`ugrep --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Zoek recursief in de huidige map en geef een lijst met passende bestanden:

`ugrep --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Zoek "fuzzy" met maximaal 3 extra, missende of verwisselende karakters in het patroon:

`ugrep --fuzzy=3 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Zoek passende gecomprimeerde bestanden, zip en tar archieven recursief in de huidige map:

`ugrep --decompress "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Zoek alleen naar bestanden met namen die overeenkomen met een passende `foo*.???` glob patroon:

`ugrep --glob="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo*.???</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Zoek alleen passende bestanden van het type C++ (gebruik `--type=list` voor een lijst van typenamen):

`ugrep --type=cpp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`
