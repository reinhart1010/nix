---
layout: page
title: common/kosmorro (français)
description: "Calcule les éphémérides et les évènements pour une date donnée, à un emplacement donné sur Terre."
content_hash: f09e0e29b4145971e704b5ecf62fc52fa3297a97
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/kosmorro.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kosmorro

Calcule les éphémérides et les évènements pour une date donnée, à un emplacement donné sur Terre.
Plus d'informations : <https://kosmorro.space>.

- Obtenir les éphémérides pour Paris (France) :

`kosmorro --latitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">48.7996</span>` --longitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.3511</span>

- Obtenir les éphémérides pour Paris (France), sur le fuseau horaire UTC+2 :

`kosmorro --latitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">48.7996</span>` --longitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.3511</span>` --timezone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Obtenir les éphémérides du 9 juin 2020 pour Paris (France) :

`kosmorro --latitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">48.7996</span>` --longitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.3511</span>` --date=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2020-06-09</span>

- Générer un fichier PDF (TeXLive doit être installé) :

`kosmorro --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier.pdf</span>
