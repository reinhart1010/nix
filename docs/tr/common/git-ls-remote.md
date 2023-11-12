---
layout: page
title: common/git-ls-remote (Türkçe)
description: "Çevrimiçi depolardaki isim ve URL bazlı referansları sıralamaya yarayan Git komutu."
content_hash: 62464e46022f7362298b191060687b863ded4aba
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-ls-remote.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-ls-remote.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-ls-remote.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git ls-remote

Çevrimiçi depolardaki isim ve URL bazlı referansları sıralamaya yarayan Git komutu.
İsim veya URL girilmemişse, varsayılan dal veya çevrimiçi dalın kökeni kullanılır.
Daha fazla bilgi için: <https://git-scm.com/docs/git-ls-remote>.

- Varsayılan çevrimiçi depodaki tüm referansları göster:

`git ls-remote`

- Varsayılan çevrimiçi depodaki yalnızca baş referanslarını göster:

`git ls-remote --heads`

- Varsayılan çevrimiçi depodaki yalnızca etiket referanslarını göster:

`git ls-remote --tags`

- Girilen isim veya URL'de bulunan çevrimiçi depodaki tüm referansları göster:

`git ls-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depo_adresi</span>

- Bir çevrimiçi depodaki referansları belirtilen desene göre göster:

`git ls-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depo_ismi</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">desen</span>`"`
