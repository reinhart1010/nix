---
layout: page
title: common/aws-ec2 (português (Brasil))
description: "Inteface de linha de comando para o AWS EC2."
content_hash: c99e3913ddd829531322c3211d7e8711657c7f45
related_topics:
  - title: Deutsch version
    url: /de/common/aws-ec2.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-ec2.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-ec2.html
    icon: bi bi-globe
---
# aws ec2

Inteface de linha de comando para o AWS EC2.
Provê capacidade computacional segura e flexível na nuvem da AWS para proporcionar um desenvolvimento e subida para produção de aplicações rapidamente.
Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html>.

- Exibe informações sobre uma insntância específica:

`aws ec2 describe-instances --instance-ids `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_da_instância</span>

- Exibe informações sobre todas as instâncias:

`aws ec2 describe-instances`

- Exibe informações sobre todos os volumes EC2:

`aws ec2 describe-volumes`

- Deleta um volume EC2:

`aws ec2 delete-volume --volume-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_volume</span>

- Cria um snapshot de um volume EC2:

`aws ec2 create-snapshot --volume-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_volume</span>

- Lista as AMIs (Imagem de Máquina da Amazon) disponíveis:

`aws ec2 describe-images`

- Lista todos os comandos EC2 disponíveis:

`aws ec2 help`

- Exibe ajuda específica para um subcomando da EC2:

`aws ec2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcomando</span>` help`
