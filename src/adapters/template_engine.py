from pathlib import Path
from docxtpl import DocxTemplate
from datetime import datetime
from uuid import uuid4

TEMPLATES_DIR = Path(__file__).parents[2] / "data" / "templates_local"
OUTPUT_DIR = Path(__file__).parents[2] / "data" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def render(template_name: str, context: dict) -> Path:
    tpl_path = TEMPLATES_DIR / f"{template_name}.docx"
    if not tpl_path.exists():
        raise FileNotFoundError(tpl_path)
    doc = DocxTemplate(tpl_path)
    doc.render(context)
    filename = f"{template_name}_{uuid4().hex[:8]}_{datetime.now():%Y%m%d}.docx"
    out_path = OUTPUT_DIR / filename
    doc.save(out_path)
    return out_path