import type { ElementType, ReactNode } from "react"

type TextProps = {
  as?: ElementType
  children: ReactNode
  className?: string
  id?: string
}

export function Text({
  as: Component = "p",
  children,
  className = "",
  id,
}: TextProps) {
  return (
    <Component className={className} id={id}>
      {children}
    </Component>
  )
}

type LinkProps = {
  children: ReactNode
  href: string
  className?: string
  ariaLabel?: string
}

export function Link({ children, href, className = "", ariaLabel }: LinkProps) {
  return (
    <a className={className} href={href} aria-label={ariaLabel}>
      {children}
    </a>
  )
}

export function Pill({
  children,
  tone = "default",
}: {
  children: ReactNode
  tone?: "default" | "accent"
}) {
  return <span className={`pill pill--${tone}`}>{children}</span>
}

export function SectionLabel({
  index,
  children,
}: {
  index: string
  children: ReactNode
}) {
  return (
    <div className="section-label" aria-hidden="true">
      <span>{index}</span>
      <span>{children}</span>
    </div>
  )
}

export function ArrowIcon({
  direction = "right",
}: {
  direction?: "right" | "down"
}) {
  return (
    <svg
      className={`icon icon--${direction}`}
      viewBox="0 0 24 24"
      aria-hidden="true"
      focusable="false"
    >
      <path d="M5 12h14M13 6l6 6-6 6" />
    </svg>
  )
}

