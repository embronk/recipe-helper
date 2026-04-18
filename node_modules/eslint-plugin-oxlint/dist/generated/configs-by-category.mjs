import { perfRules, correctnessRules, restrictionRules, styleRules, suspiciousRules, pedanticRules } from "./rules-by-category.mjs";
const pedanticConfig = {
  name: "oxlint/pedantic",
  rules: pedanticRules
};
const suspiciousConfig = {
  name: "oxlint/suspicious",
  rules: suspiciousRules
};
const styleConfig = {
  name: "oxlint/style",
  rules: styleRules
};
const restrictionConfig = {
  name: "oxlint/restriction",
  rules: restrictionRules
};
const correctnessConfig = {
  name: "oxlint/correctness",
  rules: correctnessRules
};
const perfConfig = {
  name: "oxlint/perf",
  rules: perfRules
};
const configByCategory = {
  "flat/pedantic": pedanticConfig,
  "flat/suspicious": suspiciousConfig,
  "flat/style": styleConfig,
  "flat/restriction": restrictionConfig,
  "flat/correctness": correctnessConfig,
  "flat/perf": perfConfig
};
export {
  configByCategory as default
};
