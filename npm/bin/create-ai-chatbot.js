#!/usr/bin/env node
/**
 * create-ai-chatbot — Scaffold a full-stack AI chatbot project.
 *
 * This is a thin wrapper that delegates to the Python package.
 * Requires Python 3.10+ with cookiecutter installed.
 */

import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { existsSync } from 'node:fs';

const __dirname = dirname(fileURLToPath(import.meta.url));

async function main() {
  const args = process.argv.slice(2);

  // Check if Python and cookiecutter are available
  const pythonCheck = spawn('python3', ['-c', 'import cookiecutter'], { stdio: 'pipe' });

  pythonCheck.on('close', (code) => {
    if (code !== 0) {
      console.error('ERROR: Python 3.10+ with cookiecutter is required.');
      console.error('Install with: pip install create-ai-chatbot');
      console.error('Or: pip install cookiecutter');
      process.exit(1);
    }

    // Find the template directory (relative to this script)
    const templateDir = join(__dirname, '..', '..');

    const child = spawn(
      'python3',
      ['-m', 'cookiecutter', templateDir, ...args],
      { stdio: 'inherit' }
    );

    child.on('close', (exitCode) => {
      process.exit(exitCode ?? 0);
    });
  });
}

main();
