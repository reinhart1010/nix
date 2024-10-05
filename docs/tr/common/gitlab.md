---
layout: page
title: common/gitlab (Türkçe)
description: "GitLab API'si için Ruby sarıcı ve CLI aracı."
content_hash: 3b464d68715985a5a6b9c36caa337df465414a0e
last_modified_at: 2024-10-05
related_topics:
  - title: English version
    url: /en/common/gitlab.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gitlab

GitLab API'si için Ruby sarıcı ve CLI aracı.
`ctl` gibi bazı alt komutların kendi kullanım kılavuzları vardır.
Daha fazla bilgi için: <https://narkoz.github.io/gitlab/>.

- Yeni bir proje oluştur:

`gitlab create_project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proje_ismi</span>

- Belirtilen commit ile ilgili bilgi al:

`gitlab commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proje_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_değeri</span>

- Bit CI pipeline'ındaki işler ile ilgili bilgi al:

`gitlab pipeline_jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proje_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pipeline_id'si</span>

- Belirtilen CI işini başlat:

`gitlab job_play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proje_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iş_id'si</span>
