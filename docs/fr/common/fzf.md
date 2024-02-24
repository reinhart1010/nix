---
layout: page
title: common/fzf (français)
description: "Recherche approximative en ligne de commande."
content_hash: 2f2391824476e1774cc9e1e360acd06130ea4eb0
last_modified_at: 2024-02-24
related_topics:
  - title: English version
    url: /en/common/fzf.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/fzf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fzf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fzf

Recherche approximative en ligne de commande.
Similaire à `sk`.
Plus d'informations : <https://github.com/junegunn/fzf>.

- Lance `fzf` sur tous les fichiers du répertoire spécifié :

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>` -type f | fzf`

- Démarre `fzf` pour les processus en cours :

`ps aux | fzf`

- Sélectionne plusieurs fichiers avec `Shift + Tab` et écrit dans un fichier :

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>` -type f | fzf --multi > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Lance `fzf` avec une requête donnée :

`fzf --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`"`

- Lance `fzf` sur les entrées qui commencent par core et se terminent par go, rb, ou py :

`fzf --query "^core go$ | rb$ | py$"`

- Lance `fzf` sur les entrées qui ne correspondent pas à pyc et qui correspondent exactement à travis :

`fzf --query "!pyc 'travis"`
