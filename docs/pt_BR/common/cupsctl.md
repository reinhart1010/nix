---
layout: page
title: common/cupsctl (português (Brasil))
description: "Atualiza ou consulta o cupsd.conf de um server."
content_hash: 43d6b1f3ca66cfb8cd7d6dcd7d71f122fe9764bb
last_modified_at: 2023-12-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsctl

Atualiza ou consulta o cupsd.conf de um server.
Mais informações: <https://www.cups.org/doc/man-cupsctl.html>.

- Exibe os valores de configuração atuais:

`cupsctl`

- Exibe os valores de configuração de um servidor específico:

`cupsctl -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor[:porta]</span>

- Ativar a criptografia na conexão ao scheduler:

`cupsctl -E`

- Ativa ou desativa o registro de depuração para o arquivo error_log:

`cupsctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--debug-logging|--no-debug-loging</span>

- Ativa ou desativa administração remota:

`cupsctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--remote-admin|--no-remote-admin</span>

- Exibe o estado atual do registro de depuração:

`cupsctl | grep '^_debug_logging' | awk -F= '{print $2}'`
