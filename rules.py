botscore_ruleset={
  "name": "Bot Score Ruleset",
  "description": "Ruleset for logging bot scores",
  "kind": "zone",
  "phase": "http_request_firewall_custom",
  "rules": [
    {
      "expression": "(cf.client.bot)",
      "action": "challenge",
      "description": "Challenge traffic with bot score 1",
      "enabled": False 
    }]}


















