---
layout: page
title: common/git-cherry-pick (français)
description: "Appliquer les modifications introduites par les commits existants à la branche actuelle."
content_hash: 330766fc88ca5faab82e9c71feb60f572140ebf3
last_modified_at: 2024-10-13
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
  - title: Indonesia version
    url: /id/common/git-cherry-pick.html
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
  - title: українська version
    url: /uk/common/git-cherry-pick.html
    icon: bi bi-globe
tldri18n_status: 2
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

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_1 commit_2 ...</span>

- Appliquer les changements d'un commit à la branche courante sans créer de commit :

`git cherry-pick --no-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
