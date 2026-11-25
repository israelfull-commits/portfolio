---
name: senior-portfolio-audit
description: >-
  Auditoria contínua de qualidade de portfólio de Senior Product Designer: consistência editorial,
  enquadramento executivo sem expressões defensivas, conformidade WCAG AAA, craft de imagem de estúdio,
  resolução dinâmica de assets SPA e integridade de deploy no GitHub Pages.
---

# Senior Portfolio & Case Study Audit Skill

Esta skill fornece o protocolo e a automação necessários para auditar, evoluir e garantir o padrão de excelência executiva do portfólio de **Senior Product Designer** de Israel Rozar.

---

## 1. Princípios Canônicos de Qualidade

### A. Calibre Editorial e Postura Profissional
- **Afirmação e Propriedade:** Nunca utilize termos autodepreciativos, dubitativos ou defensivos (ex.: *"conteúdo fictício"*, *"não comprova implantação"*, *"limites das evidências"*, *"relato original"*, *"amostras não se somam"*).
- **Dados Regulados (Saúde e Finanças):** Interfaces demonstrativas devem ser apresentadas sob a ótica de **anonimização para proteção de privacidade (LGPD), sigilo médico ou sigilo bancário**, preservando fielmente a hierarquia de dados e contratos de interface.
- **Rigor de Pesquisa:** Evidencie sempre a **triangulação metodológica** (ex.: pesquisa quantitativa com 121 respondentes combinada a entrevistas semiestruturadas com médicos especialistas ou consultores de investimentos).
- **Consistência Numérica Estrita:** Garanta paridade exata de números entre a vitrine da Home e as páginas de cada case (ex.: 4 distribuidoras integradas e 5 blueprints de serviço no case Neoenergia).

### B. Craft Visual e Imagens de Alta Resolução
- **Master Heroes:** Devem conter tratamento fotográfico de estúdio, multi-tier drop-shadows difusos, molduras físicas de contenção (`#102B1D`) e badges de contexto legíveis.
- **Eliminação de Bordas (Bezel Strip):** Em recortes de assets compostos (ex.: Figma), calcule as coordenadas exatas para eliminar bordas de telas e molduras antigas sem cortar textos de interface.
- **Contraste WCAG AAA:** Textos e badges sobre imagens devem garantir taxa de contraste superior a 12:1.

### C. Arquitetura SPA e Deploy Contínuo (GitHub Pages)
- **Ativos Dinâmicos:** Todo asset (`/images/`, `/icons/`, `/documents/`) deve ser envolvido pela função utilitária `assetUrl(src)` em componentes React.
- **Geração de Rotas Estáticas:** Toda rota de case deve possuir seu próprio `index.html` gerado na pasta `site/dist/cases/...` para retornar **HTTP 200 OK** direto na navegação e evitar 404 em refreshes.
- **Navegação Circular:** O rodapé de cada case deve alimentar a navegação do recrutador para o próximo case da esteira (**Einstein ➔ Itaú ➔ Claro ➔ Neoenergia ➔ Einstein**).

### D. Diretrizes UX Companion 2026 (Senior Heuristics)
- **Decisões como Unidade de Valor:** O case deve responder com clareza: quais foram as 3 decisões capitais tomadas pelo designer e quais alternativas foram rejeitadas?
- **Reenquadramento de Problema (Reframing):** Demonstrar como o problema real difere da solicitação original do briefing.
- **O que NÃO foi construído:** Identificar escopo descartado para proteger prazos, performance ou usabilidade.
- **Evidência de Liderança e Desacordo Construtivo:** Relatar navegação de tensões com PM/Engenharia e rituais de facilitação.
- **Métricas Ancoradas:** Resultados de negócio categorizados por Receita, Custo ou Risco (Conformidade).
- **Reflexão Crítica:** Conclusão com aprendizados honestos e o que seria feito diferente hoje.
- **Anti-Padrões Proibidos:** Zero "Double Diamond" genérico sem decisão, zero mosaicos de 8 métodos/personas roxas, zero "nós fizemos" vago, zero mosaico ilegível de 12 telas. Consulte [SENIOR_UX_PORTFOLIO_CANON.md](file:///c:/Users/Israel%20Rozar/Documents/ChatGPT/Portfolio/SENIOR_UX_PORTFOLIO_CANON.md).

### E. Plain Language, Zero Jargão & Estrutura STAR Documental
- **Linguagem Simples e Direta:** Proibição de jargões herméticos ou pedantes. Redija de forma factual e acessível para qualquer stakeholder.
- **Estruturação por Dados Brutos (STAR):** Narrativa baseada exclusivamente em Situação, Tarefa, Ação e Resultado concreto, sem inferências inventadas.
- **Negative Prompting Rigoroso:** Proibição de termos como *"interface amigável"*, *"mergulhar no problema"*, *"design clean"*, *"disruptivo"*, *"sinergia"*, *"revolucionário"*, *"encantar"*, *"mágica"*.
- **Substituição por Padrões Técnicos:** Heurísticas de Nielsen, princípios Gestalt, critérios WCAG 2.2 AAA e tokens de Design System.



---

## 2. Ferramenta de Auditoria Automatizada

Execute a verificação automatizada através do CLI do projeto:

```bash
python scripts/portfolio_qa_sentinel.py
```

O script verifica automaticamente:
1. Ausência de termos defensivos e rascunhos.
2. Inexistência de pontos e vírgulas sintáticos indevidos.
3. Resolução segura de ativos via `assetUrl`.
4. Consistência cruzada de números e escopo entre Home e Cases.
5. Existência de todas as rotas estáticas SPA na pasta de build (`site/dist`).

---

## 3. Checklist Pré-Publicação

Antes de qualquer commit ou push para a branch `main`:
1. `npm --prefix site run build` (garantir compilação com 0 erros).
2. `python scripts/portfolio_qa_sentinel.py` (garantir status `PASS` em todos os critérios).
3. Sincronizar arquivos para `portfolio-verde/` se aplicável.
4. `git push origin main` (dispara deploy automatizado no GitHub Actions).

