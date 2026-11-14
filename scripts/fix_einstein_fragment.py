with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''    {
      title:
        "Decisões de; design: estabilidade visual e componentes reaproveitáveis.",

      content: (
        <ol className="cp-decisions">'''

replacement = '''    {
      title:
        "Decisões de; design: estabilidade visual e componentes reaproveitáveis.",

      content: (
        <>
          <ol className="cp-decisions">'''

target_end = '''        <CaseFigure
          image={{
            src: "/images/hiae-ds-componentes-crop-1600.webp",
            width: 1600,
            height: 900,
            alt: "Documentação dos componentes DataField e ExamTitle com tokens e anatomia modular",
            caption:
              "Documentação dos componentes estruturais: DataField e ExamTitle com tokens de espaçamento e regras de anatomia modular.",
          }}
        />
      ),'''

replacement_end = '''        <CaseFigure
          image={{
            src: "/images/hiae-ds-componentes-crop-1600.webp",
            width: 1600,
            height: 900,
            alt: "Documentação dos componentes DataField e ExamTitle com tokens e anatomia modular",
            caption:
              "Documentação dos componentes estruturais: DataField e ExamTitle com tokens de espaçamento e regras de anatomia modular.",
          }}
        />
        </>
      ),'''

if target in text and target_end in text:
    text = text.replace(target, replacement, 1)
    text = text.replace(target_end, replacement_end, 1)
    with open('site/src/pages/CasePages.tsx', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Wrapped in <> and </> successfully.")
else:
    print("Could not find targets in CasePages.tsx")

