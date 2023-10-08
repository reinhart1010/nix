---
layout: page
title: common/hashcat (français)
description: "Outil de récupération de mot de passe rapide et avancé."
content_hash: 74ba7ebe04ad0d4d4de5a76539f33e2fe5f2a67a
last_modified_at: 2023-10-08
related_topics:
  - title: English version
    url: /en/common/hashcat.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># hashcat

Outil de récupération de mot de passe rapide et avancé.
Plus d'informations : <https://hashcat.net/wiki/doku.php?id=hashcat>.

- Effectue une attaque par force brute (mode 3) avec le masque hashcat par défaut :

`hashcat --hash-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_type_hash</span>` --attack-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur_hash</span>

- Effectue une attaque par force brute (mode 3) avec un motif connu de 4 chiffres :

`hashcat --hash-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_type_hash</span>` --attack-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur_hash</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">?d?d?d?d</span>`"`

- Effectue une attaque par force brute (mode 3) en utilisant au plus 8 caractères parmi tous les caractères ASCII imprimables :

`hashcat --hash-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_type_hash</span>` --attack-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` --increment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur_hash</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">?a?a?a?a?a?a?a?a</span>`"`

- Effectue une attaque par dictionnaire (mode 0) en utilisant la liste de mots RockYou d'une machine Kali Linux :

`hashcat --hash-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_type_hash</span>` --attack-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur_hash</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/share/wordlists/rockyou.txt</span>

- Effectue une attaque par dictionnaire basée sur des règles (mode 0) en utilisant la liste de mots RockYou modifiée avec des variations de mots de passe courants :

`hashcat --hash-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_type_hash</span>` --attack-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --rules-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/share/hashcat/rules/best64.rule</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur_hash</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/share/wordlists/rockyou.txt</span>

- Effectue une attaque combinée (mode 1) en utilisant la concaténation de mots provenant de deux dictionnaires personnalisés différents :

`hashcat --hash-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_type_hash</span>` --attack-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur_hash</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/dictionnaire1.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/dictionnaire2.txt</span>

- Affiche le résultat d'un hash déjà craqué :

`hashcat --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur_hash</span>
