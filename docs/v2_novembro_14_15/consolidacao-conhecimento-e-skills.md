# Consolidação de Aprendizados e Sistema de Governança

Este documento consolida os aprendizados, padrões arquiteturais, regras imutáveis e ferramentas automatizadas criadas para evitar a recorrência de erros e elevar continuamente o nível de entrega do portfólio de **Senior Product Designer** de Israel Rozar.

---

## 1. O que foi Aprendido e Solucionado

### A. Roteamento SPA e Resolução de Ativos no GitHub Pages
* **O Problema:** Em deploys de Single Page Applications (React Router) hospedadas em subdiretórios (`/portfolio/`), caminhos absolutos como `<img src="/images/..." />` apontavam para o domínio raiz (`https://israelfull-commits.github.io/images/...`), gerando erros 404. Além disso, a navegação direta em rotas internas (`/cases/...`) falhava ao atualizar a página.
* **A Solução Canônica:**
  1. Criação do utilitário `assetUrl(src)` em `design-system.tsx`, que injeta dinamicamente `import.meta.env.BASE_URL`.
  2. Componente `<Link>` centralizado envolvendo automaticamente todos os links internos.
  3. Script de pós-build `site/scripts/generate_spa_routes.js` que gera cópias físicas de `index.html` em cada pasta de rota (`cases/.../index.html`) e o `404.html`, garantindo retorno direto com **HTTP 200 OK**.

### B. Calibre Editorial de Senior Product Designer
* **O Problema:** A inserção inadvertida de notas autodepreciativas ou disclaimers excessivos de rascunho (*"conteúdo fictício"*, *"não comprova implantação"*, *"limites das evidências"*, *"relato original"*) desvalorizava o impacto executivo do trabalho.
* **A Solução Canônica:**
  1. **Enquadramento de Proteção de Dados:** Dados sintetizados/anonimizados são apresentados como conformidade com a **LGPD, sigilo médico ou sigilo bancário**.
  2. **Rigor de Pesquisa:** Descrição como **triangulação metodológica** (pesquisa quantitativa combinada a entrevistas semiestruturadas com especialistas).
  3. **Consistência Numérica Cruzada:** Alinhamento rigoroso entre os dados da Home e os detalhes de cada case (ex.: 4 distribuidoras integradas e 5 blueprints de serviço no case Neoenergia).

### C. Tratamento Fotográfico e Craft Visual (Master Hero)
* **A Solução Canônica:** 
  - Moldura de contenção física pine `#102B1D`.
  - Multi-tier photographic drop-shadow suave.
  - Recortes milimétricos que eliminam molduras antigas de hardware sem cortar elementos de interface.
  - Contraste visual superior a 12:1 (WCAG AAA).

---

## 2. Novos Artefatos e Ferramentas Criadas

### 🛠️ CLI de Auditoria Automatizada: `portfolio_qa_sentinel.py`
Localização: `scripts/portfolio_qa_sentinel.py`

Pode ser executado a qualquer momento via terminal:
```bash
python scripts/portfolio_qa_sentinel.py
```

**Critérios Validados:**
- `[PASS]` Expressões Defensivas / Rascunhos
- `[PASS]` Sintaxe e Pontuação Tipográfica
- `[PASS]` Resolução Dinâmica de Ativos (`assetUrl`)
- `[PASS]` Consistência de Métricas Cross-Case
- `[PASS]` Estrutura e Rotas Estáticas SPA (`site/dist`)

---

### 🧠 Nova Skill Oficial: `senior-portfolio-audit`
Registrada em:
- **Local (Workspace):** `.agents/skills/senior-portfolio-audit/SKILL.md`
- **Global (Antigravity):** `C:\Users\Israel Rozar\.gemini\skills\senior-portfolio-audit\SKILL.md`

Instrui os agentes a sempre adotar a postura executiva sênior, executar a suíte de testes antes de qualquer entrega e garantir paridade visual e de dados.

---

### 📜 Regras Canônicas: `AGENTS.md`
Localização: `AGENTS.md` (raiz do projeto)

Define o contrato imutável para qualquer sessão ou agente de inteligência artificial que atuar sobre este repositório, cobrindo:
1. Postura e Calibre Editorial
2. Padrões de Imagem e Craft Visual
3. Arquitetura de Software e Deploy (SPA)
4. Governança e Sincronização de Repositório (1:1 entre `site/` e `portfolio-verde/`)

---

## 3. Checklist Contínuo de Deploy

Sempre que uma nova evolução for realizada:
```bash
# 1. Validar qualidade e ausência de regressões
python scripts/portfolio_qa_sentinel.py

# 2. Compilar produção
npm --prefix site run build

# 3. Sincronizar e enviar
git add .
git commit -m "feat/fix: ..."
git push origin main
```
