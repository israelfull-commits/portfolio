with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Do documento ao')
end_pos = text.find('export const claroPresentation: CasePresentationData')
print(text[pos:pos+4000])

