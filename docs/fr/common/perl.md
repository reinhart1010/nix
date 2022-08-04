---
layout: page
title: common/perl (français)
description: "Interpréteur du langage Perl (version 5)."
content_hash: a883b3fa933e612e6522a3d25baa16269da3e224
related_topics:
  - title: English version
    url: /en/common/perl.html
    icon: bi bi-globe
---
# perl

Interpréteur du langage Perl (version 5).
Plus d'informations : <https://www.perl.org>.

- Exécuter le code contenu dans un fichier :

`perl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.pl</span>

- Vérifier la syntaxe sans exécuter le programme :

`perl -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.pl</span>

- Exécuter une expression Perl :

`perl -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression</span>

- Lancer le programme avec le debugger Perl :

`perl -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.pl</span>

- Itérer sur toutes les lignes d'un fichier, en les modifiant sur place en utilisant une expression de recherche et de remplacement :

`perl -p -i -e 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recherche</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remplacement</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Lancer une expression de recherche et remplacement sur un fichier, en sauvegardant le fichier original avec une autre extension :

`perl -p -i'.ancien' -e 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recherche</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remplacement</span>`/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Lancer une expression de recherche et remplacement sur un fichier, en sauvegardant le résultat dans un autre fichier :

`perl -p0e 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recherche</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remplacement</span>`/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_entrée</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_sortie</span>

- Lancer une expression régulière (RegEx) sur stdin, en affichant le premier groupe capturé pour chaque ligne :

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_entrée</span>` | perl -nle 'if (/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex</span>`/) { print "$1"; last;}'`
