# Bounty Protocol Documentation

## Overview

This repository runs human-agency-required bounty experiments to test detection of genuine human interaction vs. autonomous agents in open-source workflows.

## Bounty Types

### Human Agency Bounty

**Purpose**: Test human vs. bot interaction patterns  
**Payment**: Manual coordination (Tikkie, Wise, SEPA)  
**Validation**: Conversation-based verification

## Decay Schedule

Bounties use geometric decay with floor rounding:

```
Position 1: Base amount
Position 2: Base / 2
Position 3: Base / 4
Position 4: Base / 8
Position 5: Base / 16
```

Example for €20 pool:
- 1st: €10.00
- 2nd: €5.00
- 3rd: €2.50
- 4th: €1.25
- 5th: €0.62

Total: €19.37 (€0.63 remains due to floor rounding)

## Participation Rules

### Qualifying Actions

1. Post a comment demonstrating human understanding
2. Engage in back-and-forth conversation
3. Respond to clarifying questions
4. Coordinate payout details

### Disqualifying Actions

1. Automated pull requests without discussion
2. Generic LLM-generated responses
3. Copy-paste template comments
4. Bot scraper submissions
5. Link dumps without context

## Payout Process

1. Human posts qualifying comment
2. Maintainer responds to verify human interaction
3. Position and amount confirmed
4. Payment method coordinated (Tikkie, Wise, or SEPA)
5. Transfer completed
6. Confirmation posted in thread

## Anti-Gaming Measures

- No CAPTCHA (can be automated)
- No forms (can be scripted)
- Requires natural conversation flow
- Maintainer discretion on qualification
- Multiple interaction points required

## Research Goals

1. Measure human vs. agent response patterns
2. Test conversation-based verification
3. Evaluate decay incentive structures
4. Document interaction quality differences

## Issue Labels

- `bounty`: Active bounty issue
- `human_agency_required`: Human-only participation
- `reward_active`: Payout pool available

## Questions

Post in the relevant bounty issue thread. All coordination happens in public comments.
