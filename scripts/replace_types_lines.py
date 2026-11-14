with open('site/src/components/CasePresentation.tsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = None
end_idx = None
for i, l in enumerate(lines):
    if l.startswith('export type CaseImage'):
        start_idx = i
    if l.startswith('export function CaseFigure'):
        end_idx = i
        break

if start_idx is not None and end_idx is not None:
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
};

"""
    new_lines = lines[:start_idx] + [replacement] + lines[end_idx:]
    with open('site/src/components/CasePresentation.tsx', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("SUCCESS: Cleanly replaced types with robust named types!")
else:
    print(f"ERROR: Could not find indices: start={start_idx}, end={end_idx}")

