---
layout: page
title: common/git-cherry-pick (italiano)
description: "Applica al ramo corrente le modifiche introdotte da commit esistenti."
content_hash: d1d8e8ed291d543c4b85aa033bd7a4b09785c5ac
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
  - title: français version
    url: /fr/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry-pick.html
    icon: bi bi-globe
---
# git cherry-pick

Applica al ramo corrente le modifiche introdotte da commit esistenti.
Per applicare le modifiche ad un altro ramo, usa prima `git checkout` per passare al ramo desiderato.
Maggiori informazioni: <https://git-scm.com/docs/git-cherry-pick>.

- Applica un commit al ramo corrente:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Applica una sequenza di commit al ramo corrente (vedi anche `git rebase --onto`):

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_iniziale</span>`~..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_finale</span>

- Applica un insieme di commit non sequenziali al ramo corrente:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_2</span>

- Aggiungi le modifiche introdotte da un commit alla cartella di lavoro, ma senza creare un nuovo commit:

`git cherry-pick -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
