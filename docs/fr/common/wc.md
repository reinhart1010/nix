---
layout: page
title: common/wc (français)
description: "Compte les lignes, les mots ou les octets."
content_hash: 4f9b8572ca38aa5cbb3d9cdcf91b334694164176
last_modified_at: 2022-11-29
related_topics:
  - title: English version
    url: /en/common/wc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/wc.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/wc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/wc.html
    icon: bi bi-globe
---
# wc

Compte les lignes, les mots ou les octets.
Plus d'informations : <https://www.gnu.org/software/coreutils/wc>.

- Compte les lignes d'un fichier :

`wc --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Compte les mots d'un fichier :

`wc --words `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Compte les octets d'un fichier :

`wc --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Compte les caractères d'un fichier (en prenant en compte l'ensemble des caractères multi-octets) :

`wc --chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Compte les lignes, les mots et les caractères depuis l'entrée standard `stdin` :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`

- Compte la longueur en nombre de caractères de la plus grande ligne d'un fichier :

`wc --max-line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>
