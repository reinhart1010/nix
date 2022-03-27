---
layout: page
title: common/gimp (русский)
description: "GNU программа для работы с изображениями."
content_hash: dbcf88edaba1c13c482f834ede7a2864849a9121
related_topics:
  - title: English version
    url: /en/common/gimp.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gimp

GNU программа для работы с изображениями.
Смотрите также: `krita`.
Больше информации: <https://docs.gimp.org/en/gimp-fire-up.html#gimp-concepts-running-command-line>.

- Запустить GIMP:

`gimp`

- Запустить без заставки:

`gimp --no-splash`

- Открыть указанные файлы:

`gimp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/изображению1 путь/к/изображению2 ...</span>

- Запустить новый инстанс, даже если один уже запущен:

`gimp --new-instance`

- Вывести ошибки и предупреждения в консоль, вместо отображения их в диалоговом окне:

`gimp --console-messages`

- Включить обработчики сигналов отладки:

`gimp --debug-handlers`
