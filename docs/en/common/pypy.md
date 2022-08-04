---
layout: page
title: common/pypy (English)
description: "Fast and compliant alternative implementation of the Python language."
content_hash: 142210fc2de7ddf056744c295641754ad01eaa72
---
# pypy

Fast and compliant alternative implementation of the Python language.
More information: <https://doc.pypy.org>.

- Start a REPL (interactive shell):

`pypy`

- Execute script in a given Python file:

`pypy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Execute script as part of an interactive shell:

`pypy -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Execute a Python expression:

`pypy -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression</span>`"`

- Run library module as a script (terminates option list):

`pypy -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>

- Install a package using pip:

`pypy -m pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Interactively debug a Python script:

`pypy -m pdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>
