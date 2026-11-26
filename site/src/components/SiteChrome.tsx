import { ArrowIcon, ChatIcon, Link, MailIcon, Text, assetUrl } from "../design-system"

import { useEffect, useRef, useState } from "react"

export function SiteHeader({ casePage = false }: { casePage?: boolean }) {
  const [menuOpen, setMenuOpen] = useState(false)
  const [scrolled, setScrolled] = useState(false)

  const menuRef = useRef<HTMLDivElement>(null)

  const buttonRef = useRef<HTMLButtonElement>(null)

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 12)
    onScroll()
    window.addEventListener("scroll", onScroll, { passive: true })
    return () => window.removeEventListener("scroll", onScroll)
  }, [])

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

  const homeSection = (section: string) => `${casePage ? "/" : ""}#${section}`

  const navigation = [
    { label: "Cases", section: "trabalho" },

    { label: "Sobre", section: "sobre" },

  ]

  return (
    <header className={`site-header${scrolled ? " is-scrolled" : ""}`}>
      <Link className="brand" href="/#topo">
        <span className="brand-mark" aria-hidden="true">
          IR
        </span>
        <span>Israel Rozar</span>
      </Link>

      <nav className="desktop-nav" aria-label="Navegação principal">
        {navigation.map(({ label, section }) => (
          <Link key={section} href={homeSection(section)}>
            {label}
          </Link>
        ))}
        <Link
          href={assetUrl("/documents/israel-rozar-curriculo.pdf")}
          download="Israel-Rozar-Curriculo.pdf"
        >
          Currículo<span className="pf-sr-only"> (PDF)</span>
        </Link>
        <Link className="header-cta" href={homeSection("contato")}>
          Entrar em contato <ArrowIcon />
        </Link>
      </nav>

      <div
        className="mobile-nav"
        ref={menuRef}
        onBlur={(event) => {
          if (!event.currentTarget.contains(event.relatedTarget as Node | null))
            closeMenu()
        }}
      >
        <button
          ref={buttonRef}
          type="button"
          aria-expanded={menuOpen}
          aria-controls="menu-principal"
          onClick={() => setMenuOpen((open) => !open)}
        >
          {menuOpen ? "Fechar" : "Menu"}
        </button>
        <nav
          id="menu-principal"
          aria-label="Navegação móvel"
          hidden={!menuOpen}
        >
          {navigation.map(({ label, section }) => (
            <Link key={section} href={homeSection(section)} onClick={closeMenu}>
              {label}
            </Link>
          ))}
          <Link
            href={assetUrl("/documents/israel-rozar-curriculo.pdf")}
            download="Israel-Rozar-Curriculo.pdf"
            onClick={closeMenu}
          >
            Currículo<span className="pf-sr-only"> (PDF)</span>
          </Link>
          <Link href={homeSection("contato")} onClick={closeMenu}>
            Entrar em contato
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

export function openProtectedEmail() {
  const user = ["i", "r", "o", "z", "a", "r"].join("")
  const domain = ["y", "a", "h", "o", "o", ".", "c", "o", "m", ".", "b", "r"].join("")
  window.location.href = `mailto:${user}@${domain}`
}

export function ContactSection({ compact = false }: { compact?: boolean }) {
  if (compact) return (
    <section className="pf-contact-wrap pf-container" id="contato" aria-labelledby="contact-title">
      <div className="pf-contact pf-home-contact">
        <div>
          <h2 id="contact-title">Oportunidades em Product Design</h2>
          <p>Disponível para posições de Senior Product Designer e projetos de consultoria.</p>
        </div>
        <div className="pf-home-contact-actions">
          <button type="button" className="pf-button pf-button-lime" onClick={openProtectedEmail}>
            Enviar e-mail <MailIcon />
          </button>
          <a href="https://www.linkedin.com/in/israelrozar/" target="_blank" rel="noopener noreferrer">LinkedIn<span className="pf-sr-only"> (abre em nova aba)</span></a>
        </div>
      </div>
    </section>
  )
  return (
    <section
      className="pf-contact-wrap pf-container"
      id="contato"
      aria-labelledby="contact-title"
      data-name="Portfolio / Contato / Desktop"
    >
      <div className="pf-contact">
        <div className="pf-contact-label">
          <ChatIcon />
          <span>Contato</span>
        </div>
        <h2 id="contact-title">
          Vamos conversar sobre oportunidades em Product Design.
        </h2>
        <p>
          Disponível para posições de Senior Product Designer e projetos de
          consultoria em produtos digitais.
        </p>
        <div className="pf-contact-bottom">
          <button
            type="button"
            className="pf-button pf-button-lime"
            onClick={openProtectedEmail}
          >
            Enviar e-mail <MailIcon />
          </button>
          <div className="pf-contact-links">
            <a
              href={assetUrl("/documents/israel-rozar-curriculo.pdf")}
              download="Israel-Rozar-Curriculo.pdf"
            >
              Baixar currículo (PDF)
            </a>
            <span className="pf-contact-sep" aria-hidden="true">
              •
            </span>
            <a
              href="https://www.linkedin.com/in/israelrozar/"
              target="_blank"
              rel="noopener noreferrer"
            >
              LinkedIn<span className="pf-sr-only"> (abre em nova aba)</span>
            </a>
          </div>
        </div>
      </div>
    </section>
  )
}
