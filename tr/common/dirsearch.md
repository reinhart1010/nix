---
layout: page
title: common/dirsearch (Türkçe)
description: "Ağ yolu tarayıcı."
content_hash: e859b99570cf51ce0644939ea556b43a72cc952d
related_topics:
  - title: English version
    url: /en/common/dirsearch.html
    icon: bi bi-globe
---
# dirsearch

Ağ yolu tarayıcı.
Daha fazla bilgi: <https://github.com/maurosoria/dirsearch>.

- Bir ağ sunucusunu yaygın eklentiler içeren yaygın yollar için tarayın:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions-list`

- Ağ sunucularını içeren bir listeyi `.php` eklentili yaygın yollar için tarayın:

`dirsearch --url-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/url-listesi.txt</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php</span>

- Bir ağ sunucusunu yaygın eklentiler içeren belirtilen yollar için tarayın:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions-list --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/url-yol-listesi.txt</span>

- Bir ağ sunucusunu çerez kullanarak tarayın:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php</span>` --cookie `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cookie</span>

- Bir ağ sunucusunu `HEAD` HTTP metodunu kullanarak tarayın:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php</span>` --http-method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Bir ağ sunucusunu tarayın ve sonuçları bir `.json` dosyasına kaydedin:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php</span>` --json-report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/rapor_dosyası.json</span>
