---
layout: page
title: osx/systemsetup (português (Portugal))
description: "Configura as definições de Preferencias do Sistema da máquina"
content_hash: 80fe0abb64b2c9a4d07c08df61d65aba27184ad2
related_topics:
  - title: English version
    url: /en/osx/systemsetup.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/systemsetup.html
    icon: bi bi-globe
---
# systemsetup

Configura as definições de Preferencias do Sistema da máquina
Mais informações: <https://support.apple.com/guide/remote-desktop/about-systemsetup-apd95406b8d/mac>.

- Ativa autenticação remota (SSH):

`systemsetup -setremotelogin on`

- Ativa o serviço de hora de rede com um fuso horário e servidor específico:

`systemsetup -settimezone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Europe/Lisbon</span>` -setnetworktimeserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.pt.pool.ntp.org</span>` -setusingnetworktime on`

- Colaca a máquina sem dormir, reiniciando automaticamente em falta de energia ou pânico do núcleo do sistema:

`systemsetup -setsleep off -setrestartpowerfailure on -setrestartfreeze on`

- Lista os discos de inicialização validos:

`systemsetup -liststartupdisks`

- Especifica um novo disco de inicialização:

`systemsetup -setstartupdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho</span>
