---
layout: page
title: common/hyperfine (italiano)
description: "Strumento di benchmarking con interfaccia CLI."
content_hash: f0257820f7fb963f6943f7a975a6f2bdb2c1ca68
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/hyperfine.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hyperfine

Strumento di benchmarking con interfaccia CLI.
Maggiori informazioni: <https://github.com/sharkdp/hyperfine/>.

- Esegui un benchmark di base, eseguendo almeno 10 esecuzioni:

`hyperfine '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>`'`

- Esegui un benchmark comparativo:

`hyperfine '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make target1</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make target2</span>`'`

- Modifica il numero minimo di esecuzioni di benchmark:

`hyperfine --min-runs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>`'`

- Esegui benchmark con periodo di riscaldamento:

`hyperfine --warmup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>`'`

- Esegui un comando prima di ogni esecuzione di benchmark (per cancellare le cache, etc.):

`hyperfine --prepare '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make clean</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>`'`

- Esegui un benchmark in cui un singolo parametro cambia per ogni esecuzione:

`hyperfine --prepare '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make clean</span>`' --parameter-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num_threads</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make -j {num_threads}</span>`'`
