---
layout: page
title: common/dirname (Türkçe)
description: "Belirtilen dosya veya yolun ana dizinini hesaplar."
content_hash: 637f6ab9ca3b57ce7c1e9570d8d468d007dbcc27
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dirname.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dirname.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dirname.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dirname

Belirtilen dosya veya yolun ana dizinini hesaplar.
Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/dirname>.

- Belirtilen yolun ana dizinini hesapla:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya_veya_dizine/giden/yol</span>

- Birden çok yolun ana dizinini hesapla:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya_veya_dizine/giden/yol_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya_veya_dizine/giden/yol_2</span>

- Komut çıktısını yeni satır yerine NUL karakteri ile sınırlandırma (`xargs` yazılımı ile kullanırken işe yarar):

`dirname --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya_veya_dizine/giden/yol_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya_veya_dizine/giden/yol_2</span>
