import { ArrowIcon, ChatIcon, Link, MailIcon, Text } from "../design-system"

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

  const homeSection = (section: string) => `${casePage ? "/" : ""}#${section}`

  const navigation = [
    { label: "Cases", section: "trabalho" },

    { label: "Expertise", section: "sobre" },

    { label: "Trajetória", section: "experiencia" },
  ]

  return (
    <header className="site-header">
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
          href="/documents/israel-rozar-curriculo.pdf"
          download="Israel-Rozar-Curriculo.pdf"
        >
          Currículo
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
            href="/documents/israel-rozar-curriculo.pdf"
            download="Israel-Rozar-Curriculo.pdf"
            onClick={closeMenu}
          >
            Currículo
          </Link>
          <Link href={homeSection("contato")} onClick={closeMenu}>
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

export function ContactSection() {
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
          Disponível para posições seniores e projetos de consultoria em
          produtos digitais.
        </p>
        <div className="pf-contact-bottom">
          <a
            className="pf-button pf-button-lime"
            href="mailto:irozar@yahoo.com.br"
          >
            Enviar um e-mail <MailIcon />
          </a>
          <div className="pf-contact-links">
            <a
              href="/documents/israel-rozar-curriculo.pdf"
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
              LinkedIn
            </a>
            <span className="pf-contact-sep" aria-hidden="true">
              •
            </span>
            <a
              href="https://github.com/israelrozar"
              target="_blank"
              rel="noopener noreferrer"
            >
              GitHub
            </a>
            <span className="pf-contact-sep" aria-hidden="true">
              •
            </span>
            <a
              href="https://uxfol.io/israelrozar"
              target="_blank"
              rel="noopener noreferrer"
            >
              UXfolio
            </a>
          </div>
        </div>
      </div>
    </section>
  )
}
