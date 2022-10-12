---
layout: page
title: windows/pabcnetcclear (русский)
description: "Препроцессор и компилятор для исходных файлов PascalABC.NET."
content_hash: 80d9ac4f9b8955c874044c273a155f0554bc8483
related_topics:
  - title: English version
    url: /en/windows/pabcnetcclear.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/pabcnetcclear.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pabcnetcclear

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
