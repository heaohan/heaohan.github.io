// ESLint configuration for modern (v9+) ESLint
export default [
  {
    ignores: ["assets/js/staticman.js"]
  },
  {
    files: ["assets/js/**/*.js"],
    languageOptions: {
      ecmaVersion: 2021,
      sourceType: "module"
    },
    linterOptions: {
      reportUnusedDisableDirectives: true
    },
    rules: {
      // Add custom rules here
    }
  }
];
