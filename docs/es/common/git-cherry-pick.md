---
layout: page
title: common/git-cherry-pick (español)
description: "Aplica los cambios introducidos por commits existentes a la rama actual."
content_hash: b144ca1c7227671f7705b063f564529d5fc236f6
last_modified_at: 2023-06-25
related_topics:
  - title: বাংলা version
    url: /bn/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cherry-pick.html
    icon: bi bi-globe
---
# git cherry-pick

Aplica los cambios introducidos por commits existentes a la rama actual.
Para aplicar cambios a otra rama, primero utiliza `git checkout` para cambiar a la rama deseada.
Más información: <https://git-scm.com/docs/git-cherry-pick>.

- Aplica un commit a la rama actual:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Aplica un rango de commits de la rama actual (véase también `git rebase --onto`):

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_inicial</span>`~..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_final</span>

- Aplica múltiples commits no secuenciales a la rama actual:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_2</span>

- Añade los cambios de un commit al directorio de trabajo, sin crear un commit:

`git cherry-pick --no-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
