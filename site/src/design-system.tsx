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
 ; href: string

  className?: string

  ariaLabel?: string

  download?: string | boolean

  onClick?: () => void

  tabIndex?: number
}

export function Link({
  children,

  href,

  className = "",

  ariaLabel,

  download,

  onClick,

  tabIndex,
}: LinkProps) {
  return (
    <a
      className={className}
      href={href}
      aria-label={ariaLabel}
      download={download}
      onClick={onClick}
      tabIndex={tabIndex}
    >
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
 ; children: ReactNode
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
  direction?: "right" | "down" | "left" | "up"
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

export function ChatIcon({ className = "" }: { className?: string }) {
  return (
    <svg
      className={className}
      width="14"
      height="14"
      viewBox="0 0 14 14"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      aria-hidden="true"
      focusable="false"
    >
      <path
        d="M12.25 8.75C12.25 9.05942 12.1271 9.35617 11.9083 9.57496C11.6895 9.79375 11.3928 9.91667 11.0833 9.91667H4.08333L1.75 12.25V2.91667C1.75 2.60725 1.87292 2.3105 2.09171 2.09171C2.3105 1.87292 2.60725 1.75 2.91667 1.75H11.0833C11.3928 1.75 11.6895 1.87292 11.9083 2.09171C12.1271 2.3105 12.25 2.60725 12.25 2.91667V8.75Z"
        stroke="currentColor"
        strokeWidth="1.2"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  )
}

export function MailIcon({ className = "" }: { className?: string }) {
  return (
    <svg
      className={className}
      width="17"
      height="14"
      viewBox="0 0 17 14"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      aria-hidden="true"
      focusable="false"
    >
      <path
        d="M1.66667 13.3333C1.20833 13.3333 0.815972 13.1701 0.489583 12.8438C0.163194 12.5174 0 12.125 0 11.6667V1.66667C0 1.20833 0.163194 0.815972 0.489583 0.489583C0.815972 0.163194 1.20833 0 1.66667 0H15C15.4583 0 15.8507 0.163194 16.1771 0.489583C16.5035 0.815972 16.6667 1.20833 16.6667 1.66667V11.6667C16.6667 12.125 16.5035 12.5174 16.1771 12.8438C15.8507 13.1701 15.4583 13.3333 15 13.3333H1.66667M8.33333 7.5L1.66667 3.33333V11.6667H15V3.33333L8.33333 7.5ZM8.33333 5.83333L15 1.66667H1.66667L8.33333 5.83333Z"
        fill="currentColor"
      />
    </svg>
  )
}

export function DownloadIcon({ className = "" }: { className?: string }) {
  return (
    <svg
      className={className}
      width="15"
      height="15"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2.2"
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
      focusable="false"
    >
      <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
      <polyline points="7 10 12 15 17 10" />
      <line x1="12" y1="15" x2="12" y2="3" />
    </svg>
  )
}
