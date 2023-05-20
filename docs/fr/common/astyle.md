---
layout: page
title: common/astyle (français)
description: "Indente, formate, et embelli du code source pour des languages de programmation comme C, C++, C# et Java."
content_hash: fe0d6813554227e4b582760784e78c56cb9ecab9
last_modified_at: 2023-05-20
related_topics:
  - title: English version
    url: /en/common/astyle.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/astyle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/astyle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/astyle.html
    icon: bi bi-globe
---
# astyle

Indente, formate, et embelli du code source pour des languages de programmation comme C, C++, C# et Java.
Pendant l'exécution, une copie du fichier original est créé avec un ".orig" suffixé au nom de fichier original.
Plus d'informations : <http://astyle.sourceforge.net>.

- Applique le style par défaut de 4 espaces pour l'indentation et pas de changement de formatage :

`astyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_source</span>

- Applique le style Java avec le style `attached` :

`astyle --style=java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Applique le style `allman` :

`astyle --style=allman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Applique une indentation personnalisé avec des espaces. Choisi entre 2 et 20 espaces :

`astyle --indent=spaces=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_d_espaces</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Applique une indentation personnalisé avec des tabulations. Choisi entre 2 et 20 tabulations :

`astyle --indent=tab=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_tabulations</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>
