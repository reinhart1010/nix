---
layout: page
title: windows/pabcnetcclear (русский)
description: "Препроцессор и компилятор для исходных файлов PascalABC.NET."
content_hash: 80d9ac4f9b8955c874044c273a155f0554bc8483
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/pabcnetcclear.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pabcnetcclear

Препроцессор и компилятор для исходных файлов PascalABC.NET.
Больше информации: <http://pascalabc.net>.

- Скомпилировать файл с исходным кодом в исполняемый файл с тем же именем:

`pabcnetcclear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/исходного_файла.pas</span>

- Скомпилировать файл с исходным кодом в исполняемый файл с заданным именем:

`pabcnetcclear /Output:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.exe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/исходного_файла.pas</span>

- Скомпилировать файл с исходным кодом в исполняемый файл с тем же именем с/без отладочной информации:

`pabcnetcclear /Debug:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/исходного_файла.pas</span>

- Разрешить искать модули по указанному пути при компиляции файла с исходным кодом в исполняемый файл с тем же именем:

`pabcnetcclear /SearchDir:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/папки</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/исходного_файла.pas</span>

- Скомпилировать файл с исходным кодом в исполняемый файл, определив символ условной компиляции:

`pabcnetcclear /Define:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">символ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/исходного_файла.pas</span>
