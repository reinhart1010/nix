---
layout: page
title: common/gobuster (Deutsch)
description: "Findet versteckte Pfade auf Webservern und mehr."
content_hash: 51ac165a3c1b5b3f2ec813163e77f4916efbbef9
related_topics:
  - title: English version
    url: /en/common/gobuster.html
    icon: bi bi-globe
---
# gobuster

Findet versteckte Pfade auf Webservern und mehr.
Weitere Informationen: <https://github.com/OJ/gobuster>.

- Finde Verzeichnisse und Dateien, die den Wörtern der Wortliste entsprechen:

`gobuster dir --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://beispiel.com/</span>` --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Finde Subdomains:

`gobuster dns --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">beispiel.com</span>` --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Finde Amazon S3-Buckets:

`gobuster s3 --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Finde andere virtuelle Hosts eines Servers:

`gobuster vhost --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://beispiel.com/</span>` --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Fuzze den Wert eines URL-Parameters:

`gobuster fuzz --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://beispiel.com/?parameter=FUZZ</span>` --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Fuzze den Namen eines URL-Parameters:

`gobuster fuzz --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://beispiel.com/?FUZZ=wert</span>` --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>
