# Restauração visual solicitada — 02/11/2026

Referência: figma-make-reference/wu8RFWqSsQKt4SgrBqgGEf/src/index.css.

Restauradas as escalas originais de display-xl, hero-feature e case-page-hero, e todos os valores de letter-spacing que haviam sido normalizados globalmente para -0.04em. A restauração inclui títulos de seção, métricas, contato e templates dos cases.

Preservadas as correções explicitamente solicitadas de espaçamento do link Voltar, alvos clicáveis, menu acessível, prevenção de overflow, tokens de borda e dimensões de imagens. Preservados os cases, imagens e conteúdos que o usuário pediu para adicionar. Não foram reintroduzidos números sem comprovação ou os dossiês Itaú na seleção pública da Home.

Verificação: comparação de propriedades tipográficas com a referência e build de produção. Home, Einstein, Claro e Vencimentos foram conferidos por DOM em 1440 e 390 px, sem overflow horizontal. Isso não representa uma nova certificação de fidelidade visual de todos os conteúdos adicionados.

Aplicado somente em site/src/index.css. O Figma publicado permanece sem alteração nesta rodada. O pacote anterior em output/release-2026-11-02 representa o estado anterior a esta restauração e não deve ser usado como versão atual.
