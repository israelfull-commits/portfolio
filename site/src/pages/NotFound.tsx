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
      <main className="not-found" id="conteudo" tabIndex={-1}>
        <span id="topo" aria-hidden="true" />
        <Text as="span">Erro 404</Text>
        <Text as="h1">Esta página não existe.</Text>
        <Text>
          O endereço pode ter mudado ou o link acessado não está mais disponível.
        </Text>
        <Link className="button button--primary" href="/">
          Voltar ao portfólio
        </Link>
      </main>
      <SiteFooter />
    </>
  )
}
