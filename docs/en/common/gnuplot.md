---
layout: page
title: common/gnuplot (English)
description: "A graph plotter that outputs in several formats."
content_hash: 706fefa8d77dbc38edacc13f16f849c929057320
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gnuplot

A graph plotter that outputs in several formats.
More information: <http://www.gnuplot.info/>.

- Start the interactive graph plotting shell:

`gnuplot`

- Plot the graph for the specified graph definition file:

`gnuplot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/definition.plt</span>

- Set the output format by executing a command before loading the definition file:

`gnuplot -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set output "path/to/filename.png" size 1024,768</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/definition.plt</span>

- Persist the graph plot preview window after gnuplot exits:

`gnuplot --persist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/definition.plt</span>
