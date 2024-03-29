---
layout: page
title: common/git-check-ignore (français)
description: "Analyser et déboguer les fichiers ignorés / exclus (\".gitignore\") de Git."
content_hash: f32673e4550e4f925ef583c71633ee4218586be7
last_modified_at: 2024-01-03
related_topics:
  - title: English version
    url: /en/common/git-check-ignore.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-check-ignore.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-check-ignore.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-check-ignore.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-check-ignore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git check-ignore

Analyser et déboguer les fichiers ignorés / exclus (".gitignore") de Git.
Plus d'informations : <https://git-scm.com/docs/git-check-ignore>.

- Vérifie qu'un fichier ou répertoire est ignoré :

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_répertoire</span>

- Vérifie que plusieurs fichiers ou répertoires sont ignorés :

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_répertoire1 chemin/vers/fichier_ou_répertoire2 ...</span>

- Utilisez des chemins d'accès, un par ligne, de `stdin` :

`git check-ignore --stdin < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_annexe</span>

- Ne pas vérifier l'index (utilisé pour déboguer pourquoi les chemins ont été suivis et non ignorés) :

`git check-ignore --no-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_répertoire1 chemin/vers/fichier_ou_répertoire2 ...</span>

- Inclure les détails pour chaque occurrence dans le chemin :

`git check-ignore --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_répertoire1 chemin/vers/fichier_ou_répertoire2 ...</span>
