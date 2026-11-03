import { useEffect } from "react"

const PUBLIC_SITE_URL = "https://dig-next-49887630.figma.site"

const SOCIAL_IMAGE = `${PUBLIC_SITE_URL}/images/israel-rozar-social.jpg`

export function PageMeta({
  title,

  description,

  noIndex = false,
}: {
  title: string
 ; description: string

  noIndex?: boolean
}) {
  useEffect(() => {
    document.title = title

    document

      .querySelector('meta[name="robots"]')

      ?.setAttribute("content", noIndex ? "noindex, follow" : "index, follow")

    const canonicalUrl = `${PUBLIC_SITE_URL}${window.location.pathname}`

    const metadata = [
      ['meta[name="description"]', description],

      ['meta[property="og:title"]', title],

      ['meta[property="og:description"]', description],

      ['meta[property="og:url"]', canonicalUrl],

      ['meta[property="og:image"]', SOCIAL_IMAGE],

      ['meta[name="twitter:title"]', title],

      ['meta[name="twitter:description"]', description],

      ['meta[name="twitter:image"]', SOCIAL_IMAGE],
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
