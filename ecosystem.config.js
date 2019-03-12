module.exports = {
  apps : [{
    name: 'safestream-core',
    script: 'python3',
    args: ["./src/main.py"],
    interpreter: 'bash'
  },
  {
    name: 'safestream-web',
    script: 'http-server',
    args: ['images'],
    interpreter: 'bash'
  }
],
};
