---
layout: page
title: linux/certbot (português (Brasil))
description: "O agente da Let's Encrypt para obtenção e renovação de certificados TLS automaticamente."
content_hash: 191f855776129ec43c31250d46c41450d05bdd38
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/linux/certbot.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/certbot.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/certbot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# certbot

O agente da Let's Encrypt para obtenção e renovação de certificados TLS automaticamente.
Sucessor do `letsencrypt`.
Mais informações: <https://certbot.eff.org/docs/using.html>.

- Obtém um novo certificado via autorização webroot, porém sem instala-o automaticamente:

`sudo certbot certonly --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_para_webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdominio.dominio.com</span>

- Obtém um novo certificado via autorização nginx e instala-o automaticamente:

`sudo certbot --nginx --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdominio.dominio.com</span>

- Obtém um novo certificado via autorização apache e instala-o automaticamente:

`sudo certbot --apache --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdominio.dominio.com</span>

- Renova todos os certificados que expirarão em 30 dias ou menos (não esqueça de reiniciar todos os servidores que usam os certificados):

`sudo certbot renew`

- Simula a obtenção de um novo certificado, porém sem salvá-lo no disco rígido:

`sudo certbot --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_para_webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdominio.dominio.com</span>` --dry-run`

- Obtém um certificado não confiável para testes:

`sudo certbot --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_para_webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdominio.dominio.com</span>` --test-cert`
