# Checklist operacional — quatro telas

Escopo: Figma YIHybVXPe0Hfmja1hAyzQZ, home desktop370:16614, case desktop370:17047, home mobile375:366, case mobile375:892.

## Ordem de execução

1. [x] Corrigir case mobile: largura de textos, quebras herdadas, metadados, índice e leitura dos mockups.
2. [x] Corrigir destinos dos projetos e menu por seção; registrar destinos ausentes sem inventar páginas.
3. [x] Separar estilos da narrativa do portfólio dos estilos internos de mockups; normalizar cores e fontes da narrativa.
4. [x] Adaptar destaque, evidências, badges e trajetória da home mobile.
5. [x] Corrigir numeração, datas e contenção desktop.
6. [x] Executar nova inspeção visual, conferir limites e documentar resultados e pendências.

## Divisão de trabalho

- Agente case_mobile: narrativa e estrutura do case mobile.
- Agente navigation: reações, destinos e componentes de navegação.
- Agente home_responsive: homes desktop e mobile.
- Agente principal: case desktop, padrões compartilhados, integração e validação final.

## Critérios de conclusão

- Nenhum texto narrativo ultrapassa a coluna.
- Mockups miniaturizados são tratados como visão geral, com evidência ampliada ou leitura complementar legível.
- Narrativa usa estilos Portfolio v1 e paleta aprovada.
- Não substituir a identidade dos produtos mostrados nos mockups pela identidade do portfólio.
- Não ligar um projeto anunciado a outro projeto sem identificação.
- Preservar conteúdo provisório, sem inventar resultados, fontes, URLs ou informação profissional.
- Validar os quatro frames após alterações e registrar limitações de protótipo.

## Resultado de execução

Executado com três agentes e integração pelo agente principal. Verificação final nos quatro frames: zero transbordamentos detectados, zero cores da narrativa fora da paleta, zero textos narrativos sem estilo, zero textos narrativos visíveis abaixo de 12 px. Ver `VALIDACAO-QUATRO-TELAS.json` e `FIGMA-AUDIT.js` para escopo e reprodução.

- Home mobile: 9075 → 8641 px; destaque1584 →1216 px, preservando dados; evidências2×2; experiências antes da formação; badges/datas no tamanho do conteúdo.
- Case mobile: metadados305 →186 px; índice288 →212 px; texto refluído; detalhe ampliado12/14 px; aviso de projeto conceitual fora da miniatura.
- Case desktop: narrativa padronizada, resumo inline corrigido, badge P0 contido, notas editoriais ocultadas e preservadas no guia.
- Rodapés compartilhados: textos vinculados a estilos; header e contato mobile sem formatação avulsa remanescente.
- Navegação: Einstein59:2, Movimentações63:2, Hub62:2 e Campanhas64:2 usam links Figma diretos, em nova aba; não são cases mobile finalizados. Registros ficou sem rota falsa, identificado como Case em preparação.
- Menu mobile e retornos: configuração fechar → home → seção; ações aceitas pela API e relidas.

## Pendências explícitas (não bloqueiam a estrutura visual)

- [ ] Testar ações sequenciais no modo apresentação do Figma. Persistência das configurações não equivale a teste runtime.
- [ ] Preparar destino próprio de Registros de Atendimento e páginas de case responsivas finais.
- [ ] Substituir conteúdo provisório e concluir frase de Impacto Sistêmico, sem inventar dados.
- [ ] Validar teclado, zoom, leitores de tela e acessibilidade no site implementado.

## Continuação — integridade do protótipo

Foram verificadas 42 reações presentes nos quatro frames e as cinco ações do componente de menu aberto. Não foram encontrados destinos NODE inexistentes nem SCROLL_TO configurados fora da página prevista após a navegação. Links documentais de projetos usam HTTPS e apontam aos frames correspondentes no Figma.

O teste em modo apresentação foi tentado por dois recursos de controle visual, mas ambos falharam na inicialização com: `failed to write kernel assets: O sistema não pode encontrar o caminho especificado. (os error 3)`. Nenhuma interação runtime foi executada ou declarada como validada. A pendência é de infraestrutura do ambiente de automação, não de uma aprovação do usuário.

Não foram criadas páginas fictícias para concluir o destino de Registros de Atendimento, nem alterado conteúdo provisório para fabricar evidência.

Evidências em `output/checklist-final-mobile-solucao.png`, `output/checklist-final-mobile-home-destaque.png`, `output/checklist-final-desktop-resumo.png`, além das capturas de navegação e auditorias dos agentes no workspace. Novas edições exigem repetir a validação.
