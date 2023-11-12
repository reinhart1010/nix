---
layout: page
title: linux/calcurse (português (Brasil))
description: "Um calendário e agenda baseados em texto para a linha de comando."
content_hash: 7613f68229839749d238b761d4581ade4a0b8e80
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/calcurse.html
    icon: bi bi-globe
tldri18n_status: 2
---
# calcurse

Um calendário e agenda baseados em texto para a linha de comando.
Mais informações: <https://calcurse.org>.

- Iniciar o calcurse em modo interativo:

`calcurse`

- Mostrar os agendamentos e eventos para o presente dia:

`calcurse --appointment`

- Apagar todos os objetos gravados localmente e importar os objetos remotos:

`calcurse-caldav --init=keep-remote`

- Apagar todos os objetos remotos e enviar os objetos gravados localmente:

`calcurse-caldav --init=keep-local`

- Copiar os objetos gravados localmente para o servidor CalDAV e vice-versa:

`calcurse-caldav --init=two-way`
