#!/usr/bin/env node
/**
 * create-ai-chatbot — Scaffold a full-stack AI chatbot project.
 *
 * Thin wrapper that delegates to the Python CLI.
 * Install the Python package first: pip install create-ai-chatbot
 */

import { spawn } from 'node:child_process';

async function main() {
  const args = process.argv.slice(2);

  const child = spawn(
    'create-ai-chatbot',
    args,
    { stdio: 'inherit' }
  );

  child.on('close', (exitCode) => {
    if (exitCode !== 0 && exitCode !== null) {
      console.error('');
      console.error('Tip: Install the Python package first:');
      console.error('  pip install create-ai-chatbot');
    }
    process.exit(exitCode ?? 0);
  });
}

main();
