import { Link, Text } from "../design-system"
import { PageMeta } from "../components/PageMeta"
import { SiteFooter, SiteHeader } from "../components/SiteChrome"

export default function NotFound() {
  return (
    <>
      <PageMeta
        noIndex
        title="Página não encontrada — Israel Rozar"
        description="A página solicitada não foi encontrada."
      />
      <Link className="skip-link" href="#conteudo">
        Pular para o conteúdo
      </Link>
      <SiteHeader casePage />
      <main className="not-found" id="conteudo">
        <span id="topo" aria-hidden="true" />
        <Text as="span">Erro 404</Text>
        <Text as="h1">Esta página não existe.</Text>
        <Text>
          O conteúdo pode ter mudado de endereço ou ainda estar em preparação.
        </Text>
        <Link className="button button--primary" href="/">
          Voltar ao portfólio
        </Link>
      </main>
      <SiteFooter />
    </>
  )
}
