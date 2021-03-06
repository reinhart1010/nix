---
layout: page
title: common/git-cherry-pick (français)
description: "Appliquer les modifications introduites par les commits existants à la branche actuelle."
content_hash: 633d24d1f9811b58e6bc1b074aacaa9d1b1aae2b
related_topics:
  - title: বাংলা version
    url: /bn/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry-pick.html
    icon: bi bi-globe
---
# git cherry-pick

Appliquer les modifications introduites par les commits existants à la branche actuelle.
Pour appliquer les changements a une autre branche, utiliser d'abord `git checkout` pour basculer sur la branche désirée.
Plus d'informations : <https://git-scm.com/docs/git-cherry-pick>.

- Applique un commit à la branche courante :

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Appliquer une plage de commits à la branche courante (voir aussi `git rebase --onto`) :

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_commit</span>`~..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_commit</span>

- Appliquer plusieurs commits non séquentiels à la branche courante :

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_2</span>

- Appliquer les changements d'un commit à la branche courante sans créer de commit :

`git cherry-pick -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
