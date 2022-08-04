---
layout: page
title: common/ftp (français)
description: "Outils permettant d'interagir avec un serveur avec le protocole FTP."
content_hash: c43c62db8e529b8b858fd4d80bbfd58d59456772
related_topics:
  - title: English version
    url: /en/common/ftp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ftp.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ftp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ftp

Outils permettant d'interagir avec un serveur avec le protocole FTP.
Plus d'informations : <https://manned.org/ftp>.

- Se connecter à un serveur FTP :

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp.exemple.com</span>

- Passer au mode de transfert binaire (médias, fichiers compressés, etc) :

`binary`

- Transférer plusieurs fichiers sans demander de confirmation pour chaque :

`prompt off`

- Télécharger plusieurs fichiers :

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- Uploader plusieurs fichiers :

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip</span>

- Supprimer plusieurs fichiers sur le serveur distant :

`mdelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- Renommer un fichier sur le serveur distant :

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancien_fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouveau_fichier</span>
