with open('site/src/components/case-presentation.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace cp-hero-visual block
old_hero_visual = '''.cp-hero-visual {
  margin-top: clamp(2rem, 4vw, 3rem);
  padding: 2.25rem;
  border: 0.35rem solid #163a2a;
  border-radius: 2rem;
  background:
    radial-gradient(ellipse 70% 50% at 50% 0%, rgba(217, 255, 99, 0.08) 0%, transparent 60%),
    linear-gradient(165deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 249, 244, 0.85) 100%);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  box-shadow:
    inset 0 1px 1px 0 rgba(255, 255, 255, 0.9),
    0 2px 4px rgba(23, 32, 25, 0.03),
    0 12px 24px rgba(22, 58, 42, 0.08),
    0 28px 56px rgba(22, 58, 42, 0.08);
}
.cp-figure { margin: 0; min-width: 0; }
.cp-figure > a { display: flex; align-items: center; justify-content: center; min-height: 2.75rem; }
.cp-figure img { display: block; width: 100%; max-width: min(100%, var(--case-image-width, 100%)); height: auto; object-fit: contain; }
.cp-figure-crop { display: block; width: 100%; max-width: min(100%, var(--case-image-width)); height: auto; }
.cp-hero-visual .cp-figure :is(img, .cp-figure-crop) { width: auto; max-height: 40rem; }'''

new_hero_visual = '''.cp-hero-visual {
  margin-top: clamp(2rem, 4vw, 3rem);
  padding: clamp(1rem, 2vw, 1.75rem);
  border: 1px solid var(--cp-line, #d2d4ca);
  border-radius: var(--radius-lg, 1.75rem);
  background:
    radial-gradient(ellipse 80% 50% at 50% 0%, rgba(217, 255, 99, 0.06) 0%, transparent 60%),
    linear-gradient(165deg, rgba(255, 255, 255, 0.96) 0%, rgba(248, 249, 244, 0.9) 100%);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow:
    inset 0 1px 1px 0 rgba(255, 255, 255, 0.95),
    0 4px 16px rgba(23, 32, 25, 0.04),
    0 20px 48px rgba(22, 58, 42, 0.07);
  transition: transform 300ms ease, box-shadow 300ms ease;
}
.cp-hero-visual:hover {
  box-shadow:
    inset 0 1px 1px 0 rgba(255, 255, 255, 0.95),
    0 6px 20px rgba(23, 32, 25, 0.06),
    0 24px 56px rgba(22, 58, 42, 0.1);
}
.cp-hero-visual .cp-figure-btn {
  border-radius: 1.25rem;
  overflow: hidden;
  border: 1px solid rgba(23, 32, 25, 0.09);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
  background: #111814;
}
.cp-hero-visual .cp-figure :is(img, .cp-figure-crop) {
  width: 100%;
  max-width: 100%;
  height: auto;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  display: block;
}
.cp-figure { margin: 0; min-width: 0; }
.cp-figure > a { display: flex; align-items: center; justify-content: center; min-height: 2.75rem; }
.cp-figure img { display: block; width: 100%; max-width: min(100%, var(--case-image-width, 100%)); height: auto; object-fit: contain; }
.cp-figure-crop { display: block; width: 100%; max-width: min(100%, var(--case-image-width)); height: auto; }'''

if old_hero_visual in css:
    css = css.replace(old_hero_visual, new_hero_visual, 1)
    print("Updated cp-hero-visual in case-presentation.css")
else:
    print("Could not find old_hero_visual in css")

with open('site/src/components/case-presentation.css', 'w', encoding='utf-8') as f:
    f.write(css)

