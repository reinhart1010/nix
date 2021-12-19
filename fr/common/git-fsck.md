---
layout: page
title: common/git-fsck (français)
description: "Vérifier la validité et la connectivité des nœuds dans un dépôt Git."
content_hash: 4e3867ce4240716869450bd5bca3fd2c7e0b24f1
related_topics:
  - title: English version
    url: /en/common/git-fsck.html
    icon: bi bi-globe
---
# git fsck

Vérifier la validité et la connectivité des nœuds dans un dépôt Git.
N'applique aucune modification. Voir `git gc` pour nettoyer.
Plus d'informations : <https://git-scm.com/docs/git-fsck>.

- Vérifier le registre courant :

`git fsck`

- Lister tous les tags trouvés :

`git fsck --tags`

- Lister tout les nœuds racine trouvés :

`git fsck --root`
