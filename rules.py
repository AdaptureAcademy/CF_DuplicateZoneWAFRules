botscore_ruleset{
  "name": "Bot Score Ruleset",
  "description": "Ruleset for logging bot scores",
  "kind": "zone",
  "phase": "http_request_firewall_custom",
  "rules": [
    {
      "action": "log",
      "expression": "(cf.bot_management.score >= 1 and cf.bot_management.score <= 10)",
      "description": "Log traffic with bot score between 1 and 10",
      "enabled": true,
      "action_mode": "draft"
    },
    {
      "action": "log",
      "expression": "(cf.bot_management.score >= 11 and cf.bot_management.score <= 20)",
      "description": "Log traffic with bot score between 11 and 20",
      "enabled": true,
      "action_mode": "draft"
    },
    {
      "action": "log",
      "expression": "(cf.bot_management.score >= 21 and cf.bot_management.score <= 30)",
      "description": "Log traffic with bot score between 21 and 30",
      "enabled": true,
      "action_mode": "draft"
    },
    {
      "action": "log",
      "expression": "(cf.bot_management.score >= 31 and cf.bot_management.score <= 40)",
      "description": "Log traffic with bot score between 31 and 40",
      "enabled": true,
      "action_mode": "draft"
    },
    {
      "action": "log",
      "expression": "(cf.bot_management.score >= 41 and cf.bot_management.score <= 50)",
      "description": "Log traffic with bot score between 41 and 50",
      "enabled": true,
      "action_mode": "draft"
    },
    {
      "action": "log",
      "expression": "(cf.bot_management.score >= 51 and cf.bot_management.score <= 60)",
      "description": "Log traffic with bot score between 51 and 60",
      "enabled": true,
      "action_mode": "draft"
    },
    {
      "action": "log",
      "expression": "(cf.bot_management.score >= 61 and cf.bot_management.score <= 70)",
      "description": "Log traffic with bot score between 61 and 70",
      "enabled": true,
      "action_mode": "draft"
    },
    {
      "action": "log",
      "expression": "(cf.bot_management.score >= 71 and cf.bot_management.score <= 80)",
      "description": "Log traffic with bot score between 71 and 80",
      "enabled": true,
      "action_mode": "draft"
    },
    {
      "action": "log",
      "expression": "(cf.bot_management.score >= 81 and cf.bot_management.score <= 90)",
      "description": "Log traffic with bot score between 81 and 90",
      "enabled": true,
      "action_mode": "draft"
    },
    {
      "action": "log",
      "expression": "(cf.bot_management.score >= 91 and cf.bot_management.score <= 99)",
      "description": "Log traffic with bot score between 91 and 99",
      "enabled": true,
      "action_mode": "draft"
    }
  ]
}
