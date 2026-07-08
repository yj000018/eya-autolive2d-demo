# eYa AutoLive2D R&D — Key Findings

## Tools Tested

### CartoonAlive (Alibaba/Tongyi Lab)
- Paper: arXiv July 2025
- Status: NO CODE — paper-only release, GitHub has only README + assets
- GitHub: https://github.com/Human3DAIGC/CartoonAlive
- Verdict: ❌ Unusable

### See-through (shitagaki-lab)
- Paper: arXiv Feb 2026
- GitHub: https://github.com/shitagaki-lab/see-through (3.1k stars)
- HuggingFace Space: https://huggingface.co/spaces/24yearsold/see-through-demo
- Tested: ✅ Generated 24 layers + PSD from eYa source image
- Output: /home/ubuntu/eya-seethrough-output/eya_layers.psd
- Verdict: ✅ Works, some inpainting artifacts on face layer

### Stretchy Studio (MangoLion)
- GitHub: https://github.com/MangoLion/stretchystudio
- Web app: https://editor.stretchy.studio
- Local instance: http://localhost:8771 (running)
- Tested: ✅ Loaded See-through PSD, 18 layers matched, auto-rig complete
- Parameters: 40+ Live2D parameters (Eye L/R Open, Mouth Form, Angle X/Y/Z, etc.)
- Status: STAGING MODE ACTIVE — eYa rigged and ready
- Limitation: WebGL sliders not controllable via browser automation

## Current State
- Stretchy Studio running at port 8771
- eYa project named "eYa_AutoLive2D_v1" ready to save
- Save dialog open — need to click "Download File" tab then save

## Workflow Validated
See-through → PSD (24 layers) → Stretchy Studio → Auto-rig (40+ params) → Animation

## Screenshots Saved
- /home/ubuntu/eya-stretchy-demo/04_joints_manual.webp
- /home/ubuntu/eya-stretchy-demo/05_rigging_complete.webp
- /home/ubuntu/eya-stretchy-demo/06_staging_mode.webp
