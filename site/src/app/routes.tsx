import { createBrowserRouter } from "react-router"

function RouteLoading() {
  return (
    <div className="route-loading" role="status" aria-live="polite">
      Carregando portfólio…
    </div>
  )
}

export const router = createBrowserRouter([
  {
    path: "/",
    HydrateFallback: RouteLoading,
    lazy: async () => {
      const { default: Component } = await import("../pages/Home")
      return { Component }
    },
  },
  {
    path: "/cases/einstein-laudos",
    HydrateFallback: RouteLoading,
    lazy: async () => {
      const { EinsteinPresentation: Component } = await import(
        "../pages/CasePages"
      )
      return { Component }
    },
  },
  {
    path: "/cases/claro-ativacao-simplificada",
    HydrateFallback: RouteLoading,
    lazy: async () => {
      const { ClaroPresentation: Component } = await import(
        "../pages/CasePages"
      )
      return { Component }
    },
  },
  {
    path: "/cases/neoenergia-conexao-digital",
    HydrateFallback: RouteLoading,
    lazy: async () => {
      const { NeoenergiaPresentation: Component } = await import(
        "../pages/CasePages"
      )
      return { Component }
    },
  },
  {
    path: "/cases/itau/:caseSlug",
    HydrateFallback: RouteLoading,
    lazy: async () => {
      const { ItauPresentation: Component } = await import("../pages/CasePages")
      return { Component }
    },
  },
  {
    path: "*",
    HydrateFallback: RouteLoading,
    lazy: async () => {
      const { default: Component } = await import("../pages/NotFound")
      return { Component }
    },
  },
])
