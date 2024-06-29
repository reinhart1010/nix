---
layout: page
title: common/shred (Nederlands)
description: "Overschrijf bestanden om gegevens veilig te verwijderen."
content_hash: 69db6ac94cc49463493f3c5fb86ad5d7ef24f2bf
last_modified_at: 2024-06-29
related_topics:
  - title: English version
    url: /en/common/shred.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shred

Overschrijf bestanden om gegevens veilig te verwijderen.
Meer informatie: <https://www.gnu.org/software/coreutils/shred>.

- Overschrijf een bestand:

`shred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Overschrijf een bestand en toon de voortgang op het scherm:

`shred --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Overschrijf een bestand, waarbij [z]ero's in plaats van willekeurige gegevens worden achtergelaten:

`shred --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Overschrijf een bestand een specifiek aa[n]tal keren:

`shred --iterations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Overschrijf een bestand en verwijder het:

`shred --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Overschrijf een bestand 100 keer, voeg een laatste overschrijving met [z]ero's toe, verwijder het bestand na overschrijven en toon [v]erbose voortgang op het scherm:

`shred -vzun 100 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
