---
layout: page
title: common/git-worktree (Türkçe)
description: "Aynı depoya bağlı çoklu çalışan ağaçları yönet."
content_hash: 92ed0659051f555b6096f8aefe70b4b19b441bd7
related_topics:
  - title: English version
    url: /en/common/git-worktree.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-worktree.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-worktree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-worktree.html
    icon: bi bi-globe
---
# git worktree

Aynı depoya bağlı çoklu çalışan ağaçları yönet.
Daha fazla bilgi: <https://git-scm.com/docs/git-worktree>.

- Belirtilen dala sahip yeni bir dizin yarat:

`git worktree add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dizin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal</span>

- Yeni bir dala sahip yeni bir dizin yarat:

`git worktree add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dizin</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_dal</span>

- Bu depoya bağlı tüm çalışan dizinleri sırala:

`git worktree list`

- Bir çalışma ağacını (çalışma ağacı dizinini sildikten sonra) kaldır:

`git worktree prune`
