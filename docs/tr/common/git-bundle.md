---
layout: page
title: common/git-bundle (Türkçe)
description: "Cisim ve referansları bir arşive paketle."
content_hash: 05d768413cdf597c6ed6f794134809a3ee14cd1f
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-bundle.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bundle.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-bundle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-bundle.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-bundle.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git bundle

Cisim ve referansları bir arşive paketle.
Daha fazla bilgi için: <https://git-scm.com/docs/git-bundle>.

- Belirtilmiş bir dalın tüm cisim ve referanslarını içeren bir paket dosyası oluştur:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosyas.bundle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Tüm dallar için bir paket dosyası oluştur:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosyas.bundle</span>` --all`

- Mevcut daldaki en son 5 commit için bir paket dosyası oluştur:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya.bundle</span>` -5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Son 7 günü içeren bir paket dosyası oluştur:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya.bundle</span>` --since=7.days `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Bir paket dosyasının geçerli olduğunu ve mevcut depoya uygulanabileceğini doğrula:

`git bundle verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya.bundle</span>

- Bir pakette bulunan referansları sırala:

`git bundle unbundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya.bundle</span>

- Belirtilen dalı paket dosyasından çıkarıp mevcut depoya koy:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya.bundle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>
