# Auditoria das imagens — case Einstein

Data: 02/11/2026

## Veredito

As duas imagens anteriores eram boas para explicar a transformação visual, mas insuficientes para demonstrar a senioridade do processo. Elas mostravam o estado original e a proposta, porém não evidenciavam claramente pesquisa, modelagem da informação e sistematização.

## Passos avaliados

1. **Contexto e método — saudável após o ajuste.** Foi incluído o diagrama de triangulação entre pesquisa quantitativa, entrevistas qualitativas e levantamento de dados.
2. **Modelagem do problema — saudável após o ajuste.** Foi incluído um laudo anonimizado com a separação entre metodologia, resultado e conclusão diagnóstica.
3. **Sistematização — saudável após o ajuste.** Foi incluído um artefato de documentação do design system para demonstrar continuidade e manutenção.
4. **Transformação visual — forte.** O antes/depois existente continua sendo a principal prova visual da solução.
5. **Resultados — adequado com ressalvas.** As métricas permanecem acompanhadas de limites e não são apresentadas como comparação causal entre versões.
6. **Privacidade — conteúdo demonstrativo confirmado.** Nome, prontuário, leito, sexo, idade, QR code, médico e data pertencem a personagens fictícios. A proposta pode ser apresentada integralmente, sem tarjas, desde que permaneça identificada no case como reconstrução demonstrativa com conteúdo fictício.
7. **Responsividade — saudável.** Foram criadas variantes WebP e `srcSet` para mobile e desktop. A galeria utiliza uma coluna no mobile e não cria overflow horizontal.
8. **Acessibilidade estrutural — saudável.** Todas as imagens possuem textos alternativos específicos. Contraste, leitura por tecnologias assistivas e compreensão clínica não podem ser certificados apenas por inspeção visual.

## Imagens incorporadas

- `site/public/images/hiae-triangulacao-pesquisa-{720,1200}.webp`
- `site/public/images/hiae-documentacao-design-system-{800,1400}.webp`
- `site/public/images/hiae-taxonomia-laudo-{1000,2000}.webp`
- `site/public/images/hiae-laudo-original-recorte-{720}.webp` e versão 1120 px
- `site/public/images/hiae-laudo-proposta-demonstrativa-{800,1600}.webp`

## Tratamento aplicado

- Recorte exclusivo de transparências externas e áreas vazias, sem apagar conteúdo útil.
- Redimensionamento Lanczos com nitidez leve após redução.
- Compressão WebP de alta qualidade e seleção responsiva pelo navegador.
- Nenhuma alteração seletiva de cor, saturação ou iluminação: os ativos são evidências documentais e já apresentavam contraste adequado.
- Nenhuma reconstrução generativa, substituição de texto ou modificação do conteúdo demonstrativo.
- Validação em 1190 px e 375 px úteis: todas as cinco imagens carregaram, sem distorção e sem overflow horizontal.

## Materiais descartados da versão pública

- Telas com nomes completos, CPF, prontuário ou responsáveis identificáveis.
- Compilações de laudos com dados clínicos potencialmente reais.
- Imagens de benchmark sem contribuição direta para provar a solução.
- Captura do template no Word: relevante como registro operacional, mas visualmente fraca e com ruído editorial.

## Próximas oportunidades

- Substituir o mockup genérico de documentação por uma captura legível dos componentes `DataField` e `ExamTitle`, quando os frames do Figma puderem ser inspecionados.
- Adicionar uma imagem do protocolo de teste ou síntese de resultados, desde que a amostra e a métrica sejam reconciliadas.
- Se forem localizados frames originais dos componentes no Figma, substituir o mockup por exportação direta em 2×, preservando estas mesmas regras de privacidade e responsividade.
