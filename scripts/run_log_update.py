from update_changelog import append_or_create_log_entry

log_text = """### 🌟 Upgrade do Case em Destaque (Hospital Albert Einstein · UX Lead)
* **Evidência Visual da Proposta Anotada:** Integrado o preview visual de alta resolução do laudo modular (`/images/hiae-estado-proposto-anotado-preview.webp`) na coluna da direita do card em destaque, comprovando instantaneamente a entrega de Design System e arquitetura clínica.
* **Badges e Narrativa de Liderança Reforçados:** Atualizado o cabeçalho para `★ Case em destaque · Saúde` e refinada a narrativa para evidenciar o papel de UX Lead e o desafio de estruturar mais de 80 exames distintos.
* **Métricas de Discovery Integradas:** Os números de pesquisa (`14 famílias`, `121 pacientes`, `04 entrevistas`, `44 testes`) foram reorganizados em harmonia com a imagem e a assinatura de parceria (`Hospital Albert Einstein × Foursys Design`).
"""

append_or_create_log_entry("CHANGELOG.md", log_text)
append_or_create_log_entry("site/CHANGELOG.md", log_text)
print("Changelogs devidamente atualizados!")
