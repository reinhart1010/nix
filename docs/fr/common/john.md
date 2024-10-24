---
layout: page
title: common/john (français)
description: "Outil de cassage de mot de passe."
content_hash: 00092dc75d6fa04407a1d9330c75d4dd5b13a404
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/john.html
    icon: bi bi-globe
tldri18n_status: 2
---
# john

Outil de cassage de mot de passe.
Plus d'informations : <https://www.openwall.com/john/>.

- Craque les hashs de mots de passe :

`john `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/hashs.txt</span>

- Affiche les mots de passe cassés :

`john --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/hashs.txt</span>

- Affiche les mots de passe cassés des utilisateurs par identifiant d'utilisateur à partir de plusieurs fichiers :

`john --show --users=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ids_utilisateurs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/hashs1.txt chemin/vers/autres/hashs2.txt ...</span>

- Craque des hashs de mots de passe, à l'aide d'une liste de mots personnalisée :

`john --wordlist=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/liste_de_mots.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/hashs.txt</span>

- Liste des formats de hachage disponibles :

`john --list=formats`

- Craque les hashs de mots de passe, en utilisant un format de hash spécifique :

`john --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md5crypt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/hashs.txt</span>

- Craque les hashs de mots de passe, en activant les règles d'altération de mots :

`john --rules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/hashs.txt</span>

- Restaure une session de craquage interrompue à partir d'un fichier d'état, par exemple `mon_cassage.rec` :

`john --restore=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/mon_cassage.rec</span>
