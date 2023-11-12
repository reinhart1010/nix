---
layout: page
title: common/zopflipng (français)
description: "Utilitaire de compression d'images PNG."
content_hash: ffb464d1f295f2c104c4452976c91af6f644d99f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/zopflipng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zopflipng

Utilitaire de compression d'images PNG.
Plus d'informations : <https://github.com/google/zopfli>.

- Optimise une image PNG :

`zopflipng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entrée.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sortie.png</span>

- Optimise plusieurs images PNG et sauvegarde avec préfixe donné :

`zopflipng --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image3.png</span>
