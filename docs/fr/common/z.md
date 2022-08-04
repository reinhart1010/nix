---
layout: page
title: common/z (français)
description: "Recherche les répertoires les plus utilisés et permet une navigation rapide à l'aide de chaînes de caractères ou d'expressions régulières."
content_hash: 71b0813befc3829e678ec2d58f1c18acce68f575
related_topics:
  - title: English version
    url: /en/common/z.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/z.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/z.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/z.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># z

Recherche les répertoires les plus utilisés et permet une navigation rapide à l'aide de chaînes de caractères ou d'expressions régulières.
Plus d'informations : <https://github.com/rupa/z>.

- Aller dans un répertoire qui contient "foo" dans son nom :

`z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Aller dans un répertoire qui contient "foo" et "bar' dans son nom :

`z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- Aller dans le répertoire le mieux classé parmi ceux qui contiennent "foo" dans leurs noms :

`z -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Aller dans le répertoire accédé le plus récemment parmi ceux qui contiennent "foo" dans leurs noms :

`z -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Lis l'ensemble des répertoires dans la base de données `z` qui contiennent "foo" dans leurs noms :

`z -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Supprime le répertoire courant de la base de données de `z` :

`z -x .`
