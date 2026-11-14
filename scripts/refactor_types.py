with open('site/src/components/CasePresentation.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

target = """export type CaseImage = {
  src: string;
  width: number;
  height: number;
  alt: string;
  caption: string;
  previewCrop?: { x: number; y: number; width: number; height: number };
};

export type CaseNavTarget = {
  title: string;
  href: string;
  context: string;
  kicker?: string;
};

export type CasePresentationData = {
  title: string;
  context: string;
  headline: string;
  subtitle: string;
  role: string;
  team: string;
  scope: string;
  kicker?: string;
  noIndex?: boolean;
  hero?: CaseImage;
  cover?: { heading: string; items: string[]; note: string };
  prevCase?: CaseNavTarget;
  nextCase?: CaseNavTarget;
  chapters: Array<{ title: string; content: ReactNode }>;
};"""

replacement = """export type CropRect = {
  x: number;
  y: number;
  width: number;
  height: number;
};

export type CaseImage = {
  src: string;
  width: number;
  height: number;
  alt: string;
  caption: string;
  previewCrop?: CropRect;
};

export type CaseNavTarget = {
  title: string;
  href: string;
  context: string;
  kicker?: string;
};

export type CaseCover = {
  heading: string;
  items: string[];
  note: string;
};

export type CaseChapter = {
  title: string;
  content: ReactNode;
};

export type CasePresentationData = {
  title: string;
  context: string;
  headline: string;
  subtitle: string;
  role: string;
  team: string;
  scope: string;
  kicker?: string;
  noIndex?: boolean;
  hero?: CaseImage;
  cover?: CaseCover;
  prevCase?: CaseNavTarget;
  nextCase?: CaseNavTarget;
  chapters: CaseChapter[];
};"""

if target in text:
    text = text.replace(target, replacement)
    with open('site/src/components/CasePresentation.tsx', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Refactored to multi-line named types!")
else:
    print("ERROR: Target not found!")

