module.exports = {
  parserOptions: {
    parser: '@typescript-eslint/parser',
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  ignorePatterns: [
    // '.eslintrc.js',
    // 'windi.config.js',
    // 'prisma/zod',
    // '_components',
    // '_pages',
  ],
  extends: [
    'plugin:@typescript-eslint/recommended',
    'plugin:nuxt/recommended',
    'plugin:vue/vue3-recommended',
  ],
  plugins: [
    'nuxt',
  ],
  rules: {
    // 'semi': [2, 'always'],
    // 'space-infix-ops': ['error', { 'int32Hint': false }],
    'require-await': 'warn',
    '@typescript-eslint/no-unused-vars': 'warn',
    'vue/no-unused-vars': 'warn',
    'vue/multi-word-component-names': 'off',
    'vue/no-multiple-template-root': 'off',
  },
};
