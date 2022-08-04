---
layout: page
title: common/jupytext (English)
description: "Tool to convert Jupyter notebooks to plain text documents, and back again."
content_hash: aa81eba5b0d78601aa8a60eea5e82cb0558e2364
---
# jupytext

Tool to convert Jupyter notebooks to plain text documents, and back again.
More information: <https://jupytext.readthedocs.io>.

- Turn a notebook into a paired `.ipynb`/`.py` notebook:

`jupytext --set-formats ipynb,py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notebook.ipynb</span>

- Convert a notebook to a `.py` file:

`jupytext --to py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notebook.ipynb</span>

- Convert a `.py` file to a notebook with no outputs:

`jupytext --to notebook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notebook.py</span>

- Convert a `.md` file to a notebook and run it:

`jupytext --to notebook --execute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notebook.md</span>

- Update the input cells in a notebook and preserve outputs and metadata:

`jupytext --update --to notebook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notebook.py</span>

- Update all paired representations of a notebook:

`jupytext --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notebook.ipynb</span>
