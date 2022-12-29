---
layout: page
title: common/curl (français)
description: "Transfère des données depuis ou vers un serveur."
content_hash: 5ebb8a9366f7c31cd27ff39bb9157c14ae4ba3c9
last_modified_at: 2022-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/curl.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/curl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/curl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/curl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/curl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/curl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/curl.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/curl.html
    icon: bi bi-globe
---
# curl

Transfère des données depuis ou vers un serveur.
Accepte la plupart des protocoles, notamment HTTP, FTP et POP3.
Plus d'informations : <https://curl.se>.

- Télécharger le contenu d'une URL dans un fichier :

`curl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://exemple.fr</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_fichier</span>

- Télécharger le contenu d'une URL dans un fichier nommé comme indiqué par l'URL :

`curl --remote-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://exemple.fr/nom_fichier</span>

- Télécharger un fichier, en suivant les redirections, et poursuivre (reprendre) automatiquement un transfert de fichier précédent et renvoyer une erreur lors d'erreurs serveurs :

`curl --fail --remote-name --location --continue-at - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://exemple.fr/nom_fichier</span>

- Envoyer des données de formulaire encodées (requête POST de type `application/x-www-form-urlencoded`). Utiliser `--data @file_name` ou `--data @'-'` pour lire depuis STDIN :

`curl --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'nom=bob'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://exemple.fr/formulaire</span>

- Envoyer une requête avec un en-tête supplémentaire, en spécifiant la méthode HTTP :

`curl --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'X-Mon-En-Tete: 123'</span>` --request `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PUT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://exemple.fr</span>

- Envoyez des données au format JSON, en spécifiant l'en-tête content-type adéquate :

`curl --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"nom":"bob"}'</span>` --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Content-Type: application/json'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://exemple.fr/utilisateurs/1234</span>

- Fournir un nom d'utilisateur et un mot de passe pour une authentification auprès du serveur :

`curl --user identifiant:motdepasse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://exemple.fr</span>

- Fournir le certificat et la clé du client pour une ressource, en évitant la validation du certificat :

`curl --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client.pem</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cle.pem</span>` --insecure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://exemple.fr</span>
