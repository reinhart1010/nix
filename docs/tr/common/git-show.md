---
layout: page
title: common/git-show (Türkçe)
description: "Çeşitli Git nesnelerini (commit'ler, etiketler vs.) görüntüle."
content_hash: 951a6a883a8a985dd77a9bff42d9e826e4320688
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-show.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-show.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-show.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-show.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git show

Çeşitli Git nesnelerini (commit'ler, etiketler vs.) görüntüle.
Daha fazla bilgi için: <https://git-scm.com/docs/git-show>.

- Son commit'e dair bilgi (değer, mesaj, değişimler ve öbür metaveriler) göster:

`git show`

- Belirtilen commit'e dair bilgi göster:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Belirtilen etiket ile özleşen commit'e dair bilgi göster:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Dalın HEAD'indeki 3. commit'e dair bilgi göster:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal</span>`~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Commit'in mesajını diff çıktısını önleyerek tek satırda göster:

`git show --oneline -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Yalnızca değiştirilen dosyalarla ilgili istatistik (eklenen/silinen karakterler) göster:

`git show --stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Yalnızca eklenen, yeniden adlandırılan veya silinen dosyaların listesini göster:

`git show --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Bir dosyanın belirtilen sürümdeki (örneğin dal, etiket veya commit) içeriğini göster:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sürüm</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/konumu</span>
