const { chromium } = require('C:/Users/User/AppData/Roaming/npm/node_modules/@playwright/mcp/node_modules/playwright');
const fs = require('fs');
const path = require('path');

const svgDir = 'c:/Karetnikov_Lineage/public/images/heraldry/logos_svg';
const pngDir = 'c:/Karetnikov_Lineage/public/images/heraldry/logos_png';

(async () => {
  const browser = await chromium.launch({ channel: 'msedge' });
  const page = await browser.newPage({ viewport: { width: 500, height: 500 } });
  
  const files = fs.readdirSync(svgDir).filter(f => f.endsWith('.svg'));
  console.log(`Rendering ${files.length} SVGs to PNG via Edge...`);

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const svgPath = path.join(svgDir, file);
    const pngName = file.replace('.svg', '.png');
    const pngPath = path.join(pngDir, pngName);
    
    const svgContent = fs.readFileSync(svgPath, 'utf8');
    await page.setContent(`<!DOCTYPE html><html><body style="margin:0;padding:0;background:transparent;">${svgContent}</body></html>`);
    await page.screenshot({ path: pngPath, omitBackground: false });
    if ((i + 1) % 25 === 0 || i === files.length - 1) {
      console.log(`Rendered ${i + 1}/${files.length}`);
    }
  }

  await browser.close();
  console.log('Rendering complete!');
})();
