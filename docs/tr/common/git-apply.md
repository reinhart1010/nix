---
layout: page
title: common/git-apply (Türkçe)
description: "İndeks veya dosyalara yama uygula."
content_hash: 766aae950a9251c6152222368f2a92d19d4be066
last_modified_at: 2024-01-02
related_topics:
  - title: Deutsch version
    url: /de/common/git-apply.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-apply.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-apply.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-apply.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git apply

İndeks veya dosyalara yama uygula.
Daha fazla bilgi için: <https://git-scm.com/docs/git-apply>.

- Yamalanan dosyalarla ilgili mesajları yazdır:

`git apply --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Yamalanan dosyaları indekse uygula ve ekle:

`git apply --index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Uzak yama dosyası uygula:

`curl -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://ornek.com/dosya.patch</span>` | git apply`

- Çıktı için fark statistiği çıkar ve yamayı uygula:

`git apply --stat --apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Yamayı tersten uygula:

`git apply --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Yama sonucunu çalışan ağacı değiştirmeden indekste sakla:

`git apply --cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>
