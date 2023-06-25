---
layout: page
title: common/git-cherry-pick (Türkçe)
description: "Varolan commit'ler ile getirilen yenilikleri mevcut dala uygula."
content_hash: 5b89ec0d7319f584d8a15389321047ea42e83229
last_modified_at: 2023-06-25
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
  - title: italiano version
    url: /it/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry-pick.html
    icon: bi bi-globe
---
# git cherry-pick

Varolan commit'ler ile getirilen yenilikleri mevcut dala uygula.
Değişiklikleri başka bir dala aktarmak için, önce `git checkout` komutu kullanılmalıdır.
Daha fazla bilgi için: <https://git-scm.com/docs/git-cherry-pick>.

- Mevcut dala bir commit uygula:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_ismi</span>

- Mevcut dala belirtilmiş aralıktaki kadar commit uygula (ayrıca `git rebase --onto` komutunun araştırılması önerilir):

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ilk_commit</span>`~..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">son_commit</span>

- Mevcut dala birçok (ardışık olmayan) commit uygula:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_2</span>

- Bir commit'in değişikliklerini, herhangi bir yeni commit oluşturmadan çalışan dizine ekle:

`git cherry-pick --no-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
