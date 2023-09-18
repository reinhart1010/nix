---
layout: page
title: common/ssh-keygen (português (Brasil))
description: "Gera chaves SSH usadas para autenticação, logins sem senha e outras finalidades."
content_hash: 4bc0e34a288bf8be72a7a4ee6bc20444852d0e10
last_modified_at: 2023-09-18
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-keygen.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh-keygen.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-keygen.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ssh-keygen

Gera chaves SSH usadas para autenticação, logins sem senha e outras finalidades.
Mais informações: <https://man.openbsd.org/ssh-keygen>.

- Gerar uma chave interativamente:

`ssh-keygen`

- Gerar uma chave ed25519 com 32 rounds de função de derivação de chave e salvar a chave em um arquivo específico:

`ssh-keygen -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ed25519</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">32</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/nome_do_arquivo</span>

- Gerar uma chave RSA de 4096 bits com um comentário de email:

`ssh-keygen -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -C "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comentário|email</span>`"`

- Remover as chaves de um host do arquivo known_hosts (útil quando um host conhecido tem uma nova chave):

`ssh-keygen -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>

- Obter a impressão digital de uma chave em MD5 Hex:

`ssh-keygen -l -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md5</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/nome_do_arquivo</span>

- Alterar a senha de uma chave:

`ssh-keygen -p -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/nome_do_arquivo</span>

- Alterar o tipo de formato da chave (por exemplo, de formato OPENSSH para PEM), o arquivo será reescrito no local:

`ssh-keygen -p -N "" -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PEM</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/chave_privada_OpenSSH</span>

- Obter a chave pública a partir da chave secreta:

`ssh-keygen -y -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/chave_privada_OpenSSH</span>
