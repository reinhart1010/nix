---
layout: page
title: common/gitlab-runner (Türkçe)
description: "GitLab koşucuları için CLI aracı."
content_hash: b4531ac051939e9f887ca01f95616a71c6093482
related_topics:
  - title: English version
    url: /en/common/gitlab-runner.html
    icon: bi bi-globe
---
# gitlab-runner

GitLab koşucuları için CLI aracı.
Daha fazla bilgi: <https://docs.gitlab.com/runner/>.

- Bir koşucuyu kayıt ettir:

`sudo gitlab-runner register --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://gitlab.ornek.com</span>` --registration-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim</span>

- Bir koşucuyu Docker çalıştırıcısıyla kayı ettir:

`sudo gitlab-runner register --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://gitlab.ornek.com</span>` --registration-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim</span>` --executor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker</span>

- Bir koşucunun kaydını geri al:

`sudo gitlab-runner unregister --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim</span>

- Koşucu servisinin durumunu görüntüle:

`sudo gitlab-runner status`

- Koşucu servisini yeniden başlat:

`sudo gitlab-runner restart`

- Kayıt edilen koşucuların GitLab'e bağlanabilme durumlarını kontrol et:

`sudo gitlab-runner verify`
