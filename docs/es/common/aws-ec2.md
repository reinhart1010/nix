---
layout: page
title: common/aws-ec2 (español)
description: "Interfaz de línea de comandos (CLI) para AWS EC2."
content_hash: 8d8fcba75c3679d7755c8ac834b4125be4af9a5a
last_modified_at: 2023-12-10
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
  - title: português (Brasil) version
    url: /pt_BR/common/aws-ec2.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-ec2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws ec2

Interfaz de línea de comandos (CLI) para AWS EC2.
Provee capacidad de computacion segura y redimensionable en la nube de AWS, permitiendo mayor velociddad en el desarrollo e implementación de aplicaciones.
Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html>.

- Muestra información acerca de una instancia específica:

`aws ec2 describe-instances --instance-ids `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_instancia</span>

- Muestra información sobre todas las instancias:

`aws ec2 describe-instances`

- Muestra información sobre todos los volúmenes EC2:

`aws ec2 describe-volumes`

- Elimina un volumen EC2:

`aws ec2 delete-volume --volume-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_volumen</span>

- Crea una instantánea a partir de un volumen EC2:

`aws ec2 create-snapshot --volume-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_volumen</span>

- Lista las imágenes de máquina de Amazon disponibles (AMI):

`aws ec2 describe-images`

- Lista todos los comandos EC2 disponibles:

`aws ec2 help`

- Muestra la ayuda para un comando EC2 específico:

`aws ec2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcomando</span>` help`
