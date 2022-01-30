---
layout: page
title: common/gitlab-ctl (Türkçe)
description: "Çok amaçlı GitLab yönetim CLI aracı."
content_hash: 3b8f093de94a841d7ae82d105893b646db4c4e84
related_topics:
  - title: English version
    url: /en/common/gitlab-ctl.html
    icon: bi bi-globe
---
# gitlab-ctl

Çok amaçlı GitLab yönetim CLI aracı.
Daha fazla bilgi: <https://docs.gitlab.com/omnibus/maintenance/>.

- Tüm servislerin durumunu görüntüle:

`sudo gitlab-ctl status`

- Belirtilen servisin durumunu görüntüle:

`sudo gitlab-ctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx</span>

- Tüm servisleri yeniden başlat:

`sudo gitlab-ctl restart`

- Belirtilen servisi yeniden başlat:

`sudo gitlab-ctl restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx</span>

- Tüm servislerin kaydını görüntüle ve `Ctrl + C` basılana kadar okumaya devam et:

`sudo gitlab-ctl tail`

- Belirtilen servisin kaydını görüntüle:

`sudo gitlab-ctl tail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx</span>
