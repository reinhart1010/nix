---
layout: page
title: common/cupsctl (português (Brasil))
description: "Atualiza ou consulta o cupsd.conf de um server."
content_hash: 2244165e34ff892b20422533e6b721f8cbf290c0
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/cupsctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cupsctl

Atualiza ou consulta o cupsd.conf de um server.
Mais informações: <https://www.cups.org/doc/man-cupsctl.html>.

- Exibe os valores de configuração atuais:

`cupsctl`

- Exibe os valores de configuração de um servidor específico:

`cupsctl -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor[:porta]</span>

- Ativa a criptografia na conexão ao scheduler:

`cupsctl -E`

- Ativa ou desativa o registro de depuração para o arquivo error_log:

`cupsctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--debug-logging|--no-debug-loging</span>

- Ativa ou desativa administração remota:

`cupsctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--remote-admin|--no-remote-admin</span>

- Exibe o estado atual do registro de depuração:

`cupsctl | grep '^_debug_logging' | awk -F= '{print $2}'`
