#!/usr/bin/env node

const { spawn } = require('child_process');
const path = require('path');
const os = require('os');
const fs = require('fs');

console.log('🔧 LawCLI 설치를 시작합니다...');

// Python 설치 확인
function checkPython() {
  return new Promise((resolve, reject) => {
    const pythonCommands = ['python', 'python3', 'py'];
    let pythonCmd = null;

    const tryCommand = (cmd, index) => {
      if (index >= pythonCommands.length) {
        reject(new Error('Python을 찾을 수 없습니다. Python 3.8 이상을 설치해주세요.'));
        return;
      }

      const process = spawn(cmd, ['--version'], { stdio: 'pipe' });
      
      process.on('error', () => {
        tryCommand(pythonCommands[index + 1], index + 1);
      });

      process.on('close', (code) => {
        if (code === 0) {
          pythonCmd = cmd;
          resolve(pythonCmd);
        } else {
          tryCommand(pythonCommands[index + 1], index + 1);
        }
      });
    };

    tryCommand(pythonCommands[0], 0);
  });
}

// 실행 스크립트 생성
function createExecutable(pythonCmd) {
  const binDir = path.join(__dirname, 'bin');
  const scriptPath = path.join(__dirname, 'lawcli', 'cli.py');
  
  if (!fs.existsSync(binDir)) {
    fs.mkdirSync(binDir, { recursive: true });
  }

  let executableContent;
  
  if (os.platform() === 'win32') {
    // Windows batch file
    executableContent = `@echo off
${pythonCmd} "${scriptPath}" %*
`;
    fs.writeFileSync(path.join(binDir, 'lawcli.bat'), executableContent);
    fs.writeFileSync(path.join(binDir, 'lawcli'), executableContent);
  } else {
    // Unix shell script
    executableContent = `#!/bin/bash
${pythonCmd} "${scriptPath}" "$@"
`;
    fs.writeFileSync(path.join(binDir, 'lawcli'), executableContent);
    fs.chmodSync(path.join(binDir, 'lawcli'), 0o755);
  }
}

// 설치 프로세스 실행
async function install() {
  try {
    console.log('🐍 Python 확인 중...');
    const pythonCmd = await checkPython();
    console.log(`✅ Python 발견: ${pythonCmd}`);
    
    console.log('📝 실행 스크립트 생성 중...');
    createExecutable(pythonCmd);
    console.log('✅ 실행 스크립트 생성 완료');
    
    console.log('🎉 LawCLI 설치가 완료되었습니다!');
    console.log('');
    console.log('사용법:');
    console.log('  npx lawcli        - 대화형 모드로 실행');
    console.log('  npx lawcli -h     - 도움말 보기');
    console.log('');
    
  } catch (error) {
    console.error('❌ 설치 실패:', error.message);
    console.error('');
    console.error('해결 방법:');
    console.error('1. Python 3.8 이상이 설치되어 있는지 확인하세요');
    console.error('2. Python이 PATH에 추가되어 있는지 확인하세요');
    process.exit(1);
  }
}

if (require.main === module) {
  install();
}