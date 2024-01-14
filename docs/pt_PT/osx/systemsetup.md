---
layout: page
title: osx/systemsetup (português (Portugal))
description: "Configura as definições de Preferencias do Sistema da máquina."
content_hash: 6fa3f5cb9f82c31d1f21bf01f9fe878620bbd8b4
last_modified_at: 2024-01-14
related_topics:
  - title: English version
    url: /en/osx/systemsetup.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/systemsetup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemsetup

Configura as definições de Preferencias do Sistema da máquina.
Mais informações: <https://support.apple.com/guide/remote-desktop/about-systemsetup-apd95406b8d/mac>.

- Ativa autenticação remota (SSH):

`systemsetup -setremotelogin on`

- Ativa o serviço de hora de rede com um fuso horário e servidor específico:

`systemsetup -settimezone "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Europe/Lisbon</span>`" -setnetworktimeserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.pt.pool.ntp.org</span>` -setusingnetworktime on`

- Coloca a máquina sem dormir, reiniciando automaticamente em falta de energia ou pânico do núcleo do sistema:

`systemsetup -setsleep off -setrestartpowerfailure on -setrestartfreeze on`

- Lista os discos de inicialização validos:

`systemsetup -liststartupdisks`

- Especifica um novo disco de inicialização:

`systemsetup -setstartupdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho</span>
