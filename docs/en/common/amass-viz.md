---
layout: page
title: common/amass-viz (English)
description: "Visualize gathered information in a network graph."
content_hash: ff285564821c15cf4f0e5869c80e6ff832188039
---
# amass viz

Visualize gathered information in a network graph.
More information: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-viz-subcommand>.

- Generate a D3.js visualization based on database data:

`amass viz -d3 -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>

- Generate a DOT file based on database data:

`amass viz -dot -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>

- Generate a Gephi Graph Exchange XML Format (GEXF) file based on database data:

`amass viz -gexf -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>

- Generate a Graphistry JSON file based on database data:

`amass viz -graphistry -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>

- Generate a Maltego CSV file based on database data:

`amass viz -maltego -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>
