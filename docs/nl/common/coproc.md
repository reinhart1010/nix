---
layout: page
title: common/coproc (Nederlands)
description: "Bash ingebouwd commando voor het maken van interactieve asynchrone subshells."
content_hash: f674936030d2e34cabb1ef3c94b3a1913585bdd8
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/common/coproc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# coproc

Bash ingebouwd commando voor het maken van interactieve asynchrone subshells.
Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#Coprocesses>.

- Voer een subshell asynchroon uit:

`coproc { `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando1; commando2; ...</span>`; }`

- Maak een coprocess met een specifieke naam:

`coproc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam</span>` { `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando1; commando2; ...</span>`; }`

- Schrijf naar de `stdin` van een specifiek coprocess:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">invoer</span>`" >&"$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{naam</span>`[1]}"`

- Lees van de `stdout` van een specifiek coprocess:

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>` <&"$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{naam</span>`[0]}"`

- Maak een coprocess dat herhaaldelijk `stdin` leest en opdrachten op de invoer uitvoert:

`coproc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam</span>` { while read line; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando1; commando2; ...</span>`; done }`

- Maak en gebruik een coprocess dat `bc` uitvoert:

`coproc BC { bc --mathlib; }; echo "1/3" >&"${BC[1]}"; read output <&"${BC[0]}"; echo "$output"`
