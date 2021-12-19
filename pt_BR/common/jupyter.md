---
layout: page
title: common/jupyter (português (Brasil))
description: "Aplicação web para criar e compartilhar documentos que contem código, visualizações e anotações."
content_hash: 16b85093644798f38b57a2d2bcdc4fe7d6cdad05
related_topics:
  - title: English version
    url: /en/common/jupyter.html
    icon: bi bi-globe
---
# jupyter

Aplicação web para criar e compartilhar documentos que contem código, visualizações e anotações.
Usado principalmente para análise de dados, computação científica e aprendizado de máquinas (machine learning).
Mais informações: <https://jupyter.org>.

- Inicia um servidor de notebooks Jupyter no diretório atual:

`jupyter notebook`

- Abre um caderno Jupyter específico:

`jupyter notebook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.ipynb</span>

- Exporta um caderno Jupyter específico para outro formato:

`jupyter nbconvert --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|markdown|pdf|script</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.ipynb</span>

- Inicia um servidor em uma porta específica:

`jupyter notebook --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>

- Lista de servidores de notebooks atualmente em funcionamento:

`jupyter notebook list`

- Para o servidor atualmente em funcionamento:

`jupyter notebook stop`

- Inicia o JupyterLab, se instalado, no diretório atual:

`jupyter lab`
