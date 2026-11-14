import { ArrowIcon, Link, Text } from "../design-system"

export function SiteHeader({ casePage = false }: { casePage?: boolean }) {
  return (
    <header className="site-header">
      <Link className="brand" href="/#topo" ariaLabel="Ir para o início">
        <span className="brand-mark" aria-hidden="true">
          IR
        </span>
        <span>Israel Rozar</span>
      </Link>

      <nav className="desktop-nav" aria-label="Navegação principal">
        {casePage ? (
          <>
            <Link href="/#trabalho">Trabalho selecionado</Link>
            <Link href="/#experiencia">Experiência</Link>
            <Link href="/documents/israel-rozar-curriculo.pdf">Currículo</Link>
          </>
        ) : (
          <>
            <Link href="#sobre">Sobre</Link>
            <Link href="#trabalho">Trabalho</Link>
            <Link href="#experiencia">Experiência</Link>
            <Link href="/documents/israel-rozar-curriculo.pdf">Currículo</Link>
          </>
        )}
        <Link className="header-cta" href={casePage ? "/#contato" : "#contato"}>
          Contato <ArrowIcon />
        </Link>
      </nav>

      <details className="mobile-nav">
        <summary>Menu</summary>
        <nav aria-label="Navegação móvel">
          <Link href={casePage ? "/#trabalho" : "#sobre"}>
            {casePage ? "Trabalho selecionado" : "Sobre"}
          </Link>
          <Link href={casePage ? "/#experiencia" : "#trabalho"}>
            {casePage ? "Experiência" : "Trabalho"}
          </Link>
          {!casePage && <Link href="#experiencia">Experiência</Link>}
          <Link href="/documents/israel-rozar-curriculo.pdf">Currículo</Link>
          <Link href={casePage ? "/#contato" : "#contato"}>Contato</Link>
        </nav>
      </details>
    </header>
  )
}

export function SiteFooter() {
  return (
    <footer>
      <Text>© Israel Rozar · Senior Product Designer</Text>
      <Link href="#topo">
        Voltar ao topo <ArrowIcon direction="down" />
      </Link>
    </footer>
  )
}

