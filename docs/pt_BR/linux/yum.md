---
layout: page
title: linux/yum (português (Brasil))
description: "Gerenciador de pacotes utilitário para RHEL, Fedora e CentOS (para outras versões)."
content_hash: 8af5664e51e015723b9594dd1426f3fca8a50d72
last_modified_at: 2023-12-28
related_topics:
  - title: català version
    url: /ca/linux/yum.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/yum.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/yum.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/yum.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/yum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yum

Gerenciador de pacotes utilitário para RHEL, Fedora e CentOS (para outras versões).
Mais informações: <https://manned.org/yum>.

- Instala um novo pacote:

`yum install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Instala um novo pacote assumindo sim para todas as perguntas (também funciona com atualizações, ótimo para atualizações automáticas):

`yum -y install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Localiza o pacote que providência um comando particular:

`yum provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Remove um pacote:

`yum remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Exibe atualizações disponíveis para pacotes instalados:

`yum check-update`

- Atualiza pacotes instalados para as novas versões disponíveis:

`yum upgrade`
