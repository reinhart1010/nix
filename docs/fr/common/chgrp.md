---
layout: page
title: common/chgrp (français)
description: "Change la propriété de groupe des fichiers et des répertoires."
content_hash: 5c7fe1f8f97d322c757e7977731213c37e234840
related_topics:
  - title: English version
    url: /en/common/chgrp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chgrp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chgrp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chgrp.html
    icon: bi bi-globe
---
# chgrp

Change la propriété de groupe des fichiers et des répertoires.
Plus d'informations : <https://www.gnu.org/software/coreutils/chgrp>.

- Change le groupe propriétaire d'un fichier/répertoire :

`chgrp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groupe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_répertoire</span>

- Change récursivement le groupe propriétaire d'un répertoire et de son contenu :

`chgrp -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groupe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>

- Change le groupe propriétaire d'un lien symbolique :

`chgrp -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groupe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/lien_symbolique</span>

- Modifie le groupe propriétaire d'un fichier/répertoire pour qu'il corresponde à un fichier de référence :

`chgrp --reference=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_référence</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_répertoire</span>
