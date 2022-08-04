---
layout: page
title: common/git-format-patch (Türkçe)
description: "`.patch` dosyaları oluştur. Commit'leri e-posta olarak gönderirken işe yarar."
content_hash: 1b1e889f248f06b5c1c1e79c9bd76fa062123f42
related_topics:
  - title: English version
    url: /en/common/git-format-patch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-format-patch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-format-patch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-format-patch.html
    icon: bi bi-globe
---
# git format-patch

`.patch` dosyaları oluştur. Commit'leri e-posta olarak gönderirken işe yarar.
Ayrıca benzer bir komut olan `git am` sayfasına bakılması önerilir.
Daha fazla bilgi: <https://git-scm.com/docs/git-format-patch>.

- Gönderilmemiş tüm commit'ler için otomatik olarak adlandırılan bir `.patch` dosyası oluştur:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>

- stdout'daki belirtilen 2 revizyon arasındaki tüm commit'ler için bir `.patch` dosyası oluştur:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revizyon_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revizyon_2</span>

- Son 3 commit için bit `.patch` dosyası oluştur:

`git format-patch -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>
