---
layout: page
title: common/mosquitto (português (Brasil))
description: "Um broker de MQTT."
content_hash: 3b8ada9c3dc6981cebc0e08398826043b83bec09
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/mosquitto.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mosquitto

Um broker de MQTT.
Mais informações: <https://mosquitto.org/>.

- Inicia mosquitto:

`mosquitto`

- Especifica um arquivo de configuração para usar:

`mosquitto --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.conf</span>

- Escuta em uma porta específica:

`mosquitto --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8883</span>

- Cria um processo rodando em background:

`mosquitto --daemon`
