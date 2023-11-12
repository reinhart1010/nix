---
layout: page
title: common/gitlab-ctl (Türkçe)
description: "Çok amaçlı GitLab yönetim CLI aracı."
content_hash: 10a70fb59fb269aa588770a21ffc4491401bc270
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/gitlab-ctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gitlab-ctl

Çok amaçlı GitLab yönetim CLI aracı.
Daha fazla bilgi için: <https://docs.gitlab.com/omnibus/maintenance/>.

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
