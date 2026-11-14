import { useEffect } from "react"

export function PageMeta({
  title,
  description,
}: {
  title: string
  description: string
}) {
  useEffect(() => {
    document.title = title
    const metadata = [
      ['meta[name="description"]', description],
      ['meta[property="og:title"]', title],
      ['meta[property="og:description"]', description],
      ['meta[name="twitter:title"]', title],
      ['meta[name="twitter:description"]', description],
    ]

    metadata.forEach(([selector, content]) => {
      document.querySelector(selector)?.setAttribute("content", content)
    })
  }, [description, title])

  return null
}

