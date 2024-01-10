---
layout: page
title: common/git-cherry-pick (español)
description: "Aplica los cambios introducidos por confirmaciones existentes a la rama actual."
content_hash: bd422aa71ace34da70ad3daaef7d24e604075cea
last_modified_at: 2024-01-10
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
tldri18n_status: 2
---
# git cherry-pick

Aplica los cambios introducidos por confirmaciones existentes a la rama actual.
Para aplicar cambios a otra rama, primero utiliza `git checkout` para cambiar a la rama deseada.
Más información: <https://git-scm.com/docs/git-cherry-pick>.

- Aplica una confirmación a la rama actual:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>

- Aplica un rango de confirmaciones de la rama actual (véase también `git rebase --onto`):

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación_inicial</span>`~..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación_final</span>

- Aplica múltiples confirmaciones no secuenciales a la rama actual:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación_2</span>

- Añade los cambios de una confirmación al directorio de trabajo, sin crear una confirmación:

`git cherry-pick --no-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>
