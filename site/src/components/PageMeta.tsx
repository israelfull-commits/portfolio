import { useEffect } from "react"
import { assetUrl } from "../design-system"

export function PageMeta({
  title,

  description,

  noIndex = false,
}: {
  title: string
  description: string

  noIndex?: boolean
}) {
  useEffect(() => {
    document.title = title

    document.documentElement.lang = "pt-BR"

    const publicSiteUrl = window.location.origin

    const socialImage = new URL(
      assetUrl("/images/israel-rozar-social.jpg"),
      publicSiteUrl,
    ).href

    document

      .querySelector('meta[name="robots"]')

      ?.setAttribute("content", noIndex ? "noindex, follow" : "index, follow")

    const canonicalUrl = new URL(window.location.pathname, publicSiteUrl).href

    const metadata = [
      ['meta[name="description"]', description],

      ['meta[property="og:title"]', title],

      ['meta[property="og:description"]', description],

      ['meta[property="og:url"]', canonicalUrl],

      ['meta[property="og:image"]', socialImage],

      ['meta[name="twitter:title"]', title],

      ['meta[name="twitter:description"]', description],

      ['meta[name="twitter:image"]', socialImage],
    ]

    metadata.forEach(([selector, content]) => {
      document.querySelector(selector)?.setAttribute("content", content)
    })

    document

      .querySelector('link[rel="canonical"]')

      ?.setAttribute("href", canonicalUrl)
  }, [description, title, noIndex])

  return null
}
