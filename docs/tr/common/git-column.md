---
layout: page
title: common/git-column (Türkçe)
description: "Kolonlarda veri görüntüle."
content_hash: 30d275091d476b5a217ad03deda09e495340a26a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-column.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git column

Kolonlarda veri görüntüle.
Daha fazla bilgi için: <https://git-scm.com/docs/git-column>.

- Standart çıktıyı çoklu kolonlar olarak biçimlendir:

`ls | git column --mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column</span>

- Standart çıktıyı maksimum `100` birim sütun genişliğinde biçimlendir:

`ls | git column --mode=column --width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Standart çıktıyı maksimum `30` birimlik boşluğa sahip situnlar olacak şekilde biçimlendir:

`ls | git column --mode=column --padding=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
