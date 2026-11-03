import { ArrowIcon, Link, Text } from "../design-system"
import { useEffect, useRef, useState } from "react"

export function SiteHeader({ casePage = false }: { casePage?: boolean }) {
  const [menuOpen, setMenuOpen] = useState(false)
  const menuRef = useRef<HTMLDivElement>(null)
  const buttonRef = useRef<HTMLButtonElement>(null)

  useEffect(() => {
    if (menuOpen)
      menuRef.current?.querySelector<HTMLAnchorElement>("nav a")?.focus()
    const handleKeydown = (event: KeyboardEvent) => {
      if (event.key === "Escape" && menuOpen) {
        setMenuOpen(false)
        buttonRef.current?.focus()
      }
    }
    const handlePointerDown = (event: PointerEvent) => {
      if (menuOpen && !menuRef.current?.contains(event.target as Node))
        setMenuOpen(false)
    }
    document.addEventListener("keydown", handleKeydown)
    document.addEventListener("pointerdown", handlePointerDown)
    return () => {
      document.removeEventListener("keydown", handleKeydown)
      document.removeEventListener("pointerdown", handlePointerDown)
    }
  }, [menuOpen])

  const closeMenu = () => setMenuOpen(false)

  return (
    <header className="site-header">
      <Link className="brand" href="/#topo">
        <span className="brand-mark" aria-hidden="true">
          IR
        </span>
        <span>Israel Rozar</span>
      </Link>

      <nav className="desktop-nav" aria-label="Navegação principal">
        {casePage ? (
          <>
            <Link href="/#trabalho">Cases</Link>
            <Link href="/#experiencia">Experiência</Link>
            <Link
              href="/documents/israel-rozar-curriculo.pdf"
              download="Israel-Rozar-Curriculo.pdf"
            >
              Currículo
            </Link>
          </>
        ) : (
          <>
            <Link href="#sobre">Sobre</Link>
            <Link href="#trabalho">Cases</Link>
            <Link href="#experiencia">Experiência</Link>
            <Link
              href="/documents/israel-rozar-curriculo.pdf"
              download="Israel-Rozar-Curriculo.pdf"
            >
              Currículo
            </Link>
          </>
        )}
        <Link className="header-cta" href={casePage ? "/#contato" : "#contato"}>
          Contato <ArrowIcon />
        </Link>
      </nav>

      <div className="mobile-nav" ref={menuRef}>
        <button
          ref={buttonRef}
          type="button"
          aria-expanded={menuOpen}
          aria-controls="menu-principal"
          onClick={() => setMenuOpen((open) => !open)}
        >
          Menu
        </button>
        <nav
          id="menu-principal"
          aria-label="Navegação móvel"
          hidden={!menuOpen}
        >
          <Link href={casePage ? "/#trabalho" : "#sobre"} onClick={closeMenu}>
            {casePage ? "Cases" : "Sobre"}
          </Link>
          <Link
            href={casePage ? "/#experiencia" : "#trabalho"}
            onClick={closeMenu}
          >
            {casePage ? "Experiência" : "Cases"}
          </Link>
          {!casePage && (
            <Link href="#experiencia" onClick={closeMenu}>
              Experiência
            </Link>
          )}
          <Link
            href="/documents/israel-rozar-curriculo.pdf"
            download="Israel-Rozar-Curriculo.pdf"
            onClick={closeMenu}
          >
            Currículo
          </Link>
          <Link href={casePage ? "/#contato" : "#contato"} onClick={closeMenu}>
            Contato
          </Link>
        </nav>
      </div>
    </header>
  )
}

export function SiteFooter() {
  return (
    <footer>
      <Text>© Israel Rozar · Senior Product Designer</Text>
      <Link href="#topo">
        Voltar ao topo <ArrowIcon direction="up" />
      </Link>
    </footer>
  )
}
