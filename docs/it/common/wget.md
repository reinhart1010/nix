---
layout: page
title: common/wget (italiano)
description: "Scarica file dal Web."
content_hash: 0d7e2709071fd696a87e81c459ccebf29a23d331
related_topics:
  - title: English version
    url: /en/common/wget.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/wget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/wget.html
    icon: bi bi-globe
---
# wget

Scarica file dal Web.
Supporta HTTP, HTTPS, FTP.
Maggiori informazioni: <https://www.gnu.org/software/wget>.

- Scarica il contenuto dell'URL in un file (dal nome "abcd" in questo caso):

`wget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://esempio.com/abcd</span>

- Scarica il contenuto dell'URL in un file (dal nome "efgh" in questo caso):

`wget --output-document `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">efgh</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://esempio.com/abcd</span>

- Scarica una singola pagina web e tutte le sue risorse (script, immagini, stili, ecc..) aspettando 3 secondi dopo ogni richiesta:

`wget --page-requisites --convert-links --wait=3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://esempio.com/pagina_web.html</span>

- Scarica tutti i file elencati nella directory e nelle sue sotto-directory (non scarica gli elementi incorporati nella pagina):

`wget --mirror --no-parent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://esempio.com/unqualchepercorso/</span>

- Limita la velocità di download e il numero di tentativi di connessione:

`wget --limit-rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300k</span>` --tries=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://esempio.com/unqualchepercorso/</span>

- Scarica un file da un server HTTP trasmettendo le credenziali tramite Basis Auth (funzione anche con FTP):

`wget --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_utente</span>` --password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://esempio.com</span>

- Riprende un download incompleto:

`wget --continue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://esempio.com</span>

- Scarica tutti gli URL contenuti in un file di testo in una directory specificata:

`wget --directory-prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>` --input-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lista_di_URL.txt</span>
