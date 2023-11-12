---
layout: page
title: windows/msiexec (русский)
description: "Установка, обновление, восстановление или удаление программ Windows через пакеты установки MSI и MSP."
content_hash: 2b8e0f8894907409a056084ebaa5b0e5f4fd98f9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/msiexec.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/msiexec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# msiexec

Установка, обновление, восстановление или удаление программ Windows через пакеты установки MSI и MSP.
Больше информации: <https://learn.microsoft.com/windows-server/administration/windows-commands/msiexec>.

- Установить программу из MSI-пакета:

`msiexec /package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.msi</span>

- Установить MSI-пакет с веб-сайта:

`msiexec /package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/installer.msi</span>

- Установить MSP-пакет с обновлением (патчем):

`msiexec /update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.msp</span>

- Удалить программу или обновление, используя соответствующий пакет MSI или MSP:

`msiexec /uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>
