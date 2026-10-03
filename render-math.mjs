import fs from 'node:fs';
import katex from 'katex';
const formulas = JSON.parse(fs.readFileSync(0, 'utf8'));
const result = formulas.map(([tex, displayMode]) => katex.renderToString(tex, {
  displayMode, throwOnError: true, trust: false, strict: 'error',
  output: 'htmlAndMathml', maxExpand: 1000
}));
process.stdout.write(JSON.stringify(result));
