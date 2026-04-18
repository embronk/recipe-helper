"use strict";
const rulesByCategory = require("./rules-by-category.cjs");
const pedanticConfig = {
  name: "oxlint/pedantic",
  rules: rulesByCategory.pedanticRules
};
const suspiciousConfig = {
  name: "oxlint/suspicious",
  rules: rulesByCategory.suspiciousRules
};
const styleConfig = {
  name: "oxlint/style",
  rules: rulesByCategory.styleRules
};
const restrictionConfig = {
  name: "oxlint/restriction",
  rules: rulesByCategory.restrictionRules
};
const correctnessConfig = {
  name: "oxlint/correctness",
  rules: rulesByCategory.correctnessRules
};
const perfConfig = {
  name: "oxlint/perf",
  rules: rulesByCategory.perfRules
};
const configByCategory = {
  "flat/pedantic": pedanticConfig,
  "flat/suspicious": suspiciousConfig,
  "flat/style": styleConfig,
  "flat/restriction": restrictionConfig,
  "flat/correctness": correctnessConfig,
  "flat/perf": perfConfig
};
module.exports = configByCategory;
