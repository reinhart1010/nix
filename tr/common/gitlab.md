---
layout: page
title: common/gitlab (Türkçe)
description: "GitLab API'si için Ruby sarıcı ve CLI aracı."
content_hash: 7878f8d2a38812fff5b794099806db9bd78fb96c
related_topics:
  - title: English version
    url: /en/common/gitlab.html
    icon: bi bi-globe
---
# gitlab

GitLab API'si için Ruby sarıcı ve CLI aracı.
`gitlab ctl` gibi bazı alt komutların kendi kullanım kılavuzları vardır.
Daha fazla bilgi: <https://narkoz.github.io/gitlab/>.

- Yeni bir proje oluştur:

`gitlab create_project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proje_ismi</span>

- Belirtilen commit ile ilgili bilgi al:

`gitlab commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proje_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_değeri</span>

- Bit CI pipeline'ındaki işler ile ilgili bilgi al:

`gitlab pipeline_jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proje_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pipeline_id'si</span>

- Belirtilen CI işini başlat:

`gitlab job_play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proje_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iş_id'si</span>
