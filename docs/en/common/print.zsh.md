---
layout: page
title: common/print.zsh (English)
description: "Z Shell (`zsh`) builtin. Prints arguments, similar to `echo`."
content_hash: 765ff9370e933c89b0f00c9b6487e0e3ce5cee9c
last_modified_at: 2025-03-02
tldri18n_status: 2
---
# print

Z Shell (`zsh`) builtin. Prints arguments, similar to `echo`.
See also: `echo`, `printf`, `zsh`.
More information: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>.

- Print input:

`print "Hello" "World"`

- Print separated by newline(s):

`print -l "Line1" "Line 2" "Line3"`

- Print without trailing newline:

`print -n "Hello"; print "World"`

- Enable backslash escapes:

`print -e "Line 1\nLine2"`

- Print arguments as described by `printf` (for greater portability across shells, consider using the `printf` command instead):

`print -f "%s is %d years old.\n" "Alice" 30`
