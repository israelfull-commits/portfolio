import { createBrowserRouter } from "react-router"

export const router = createBrowserRouter([
  {
    path: "/",
    lazy: async () => {
      const { default: Component } = await import("../pages/Home")
      return { Component }
    },
  },
  {
    path: "/cases/einstein-laudos",
    lazy: async () => {
      const { default: Component } = await import("../pages/EinsteinCase")
      return { Component }
    },
  },
  {
    path: "/cases/:caseSlug",
    lazy: async () => {
      const { default: Component } = await import(
        "../pages/ItauPreparationCase"
      )
      return { Component }
    },
  },
  {
    path: "*",
    lazy: async () => {
      const { default: Component } = await import("../pages/NotFound")
      return { Component }
    },
  },
])

