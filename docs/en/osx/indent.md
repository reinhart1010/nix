---
layout: page
title: osx/indent (English)
description: "Change the appearance of a C/C++ program by inserting or deleting whitespace."
content_hash: 58bfc3007e684cf8ef6d1350666e1481126cd915
last_modified_at: 2024-01-22
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/osx/indent.html
    icon: bi bi-globe
tldri18n_status: 2
---
# indent

Change the appearance of a C/C++ program by inserting or deleting whitespace.
More information: <https://keith.github.io/xcode-man-pages/indent.1.html>.

- Format C/C++ source according to the Berkeley style:

`indent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/indented_file.c</span>` -nbad -nbap -bc -br -c33 -cd33 -cdb -ce -ci4 -cli0 -di16 -fc1 -fcb -i4 -ip -l75 -lp -npcs -nprs -psl -sc -nsob -ts8`

- Format C/C++ source according to the style of Kernighan & Ritchie (K&R):

`indent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/indented_file.c</span>` -nbad -bap -nbc -br -c33 -cd33 -ncdb -ce -ci4 -cli0 -cs -d0 -di1 -nfc1 -nfcb -i4 -nip -l75 -lp -npcs -nprs -npsl -nsc -nsob`
