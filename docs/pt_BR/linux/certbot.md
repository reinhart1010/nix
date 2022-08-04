---
layout: page
title: linux/certbot (português (Brasil))
description: "O agente da Let's Encrypt para obtenção e renovação de certificados TLS automaticamente."
content_hash: cac9af36558b6e240750f6b85cf3486412a3a7c3
related_topics:
  - title: Deutsch version
    url: /de/linux/certbot.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/certbot.html
    icon: bi bi-globe
---
# certbot

O agente da Let's Encrypt para obtenção e renovação de certificados TLS automaticamente.
Sucessor do `letsencrypt`.
Mais informações: <https://certbot.eff.org/docs/using.html>.

- Obter um novo certificado via autorização webroot, porém sem instalá-lo automaticamente:

`sudo certbot certonly --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_para_webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdominio.dominio.com</span>

- Obter um novo certificado via autorização nginx e instalá-lo automaticamente:

`sudo certbot --nginx --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdominio.dominio.com</span>

- Obter um novo certificado via autorização apache e instalá-lo automaticamente:

`sudo certbot --apache --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdominio.dominio.com</span>

- Renovar todos os certificados que expirarão em 30 dias ou menos (não esqueça de reiniciar todos os servidores que usam os certificados):

`sudo certbot renew`

- Simular a obtenção de um novo certificado, porém sem salvá-lo no disco rígido:

`sudo certbot --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_para_webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdominio.dominio.com</span>` --dry-run`

- Obter um certificado não confiável para testes:

`sudo certbot --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_para_webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdominio.dominio.com</span>` --test-cert`
