# -*- coding: utf-8 -*-
# calculations.py

from config import (
    MODEL_PRICES, ORGEN_ROUTING, TOKENS_PER_DAY,
    WORKING_DAYS, INPUT_OUTPUT_RATIO, PLATFORM_FEE, MANUAL_SAVINGS,
)


def calc_tokens_per_month(user_type, count):
    return TOKENS_PER_DAY[user_type] * WORKING_DAYS * count


def calc_cost_for_routing(tokens, routing, ratio):
    total_cost = 0.0
    for route in routing:
        model_name    = route["model"]
        share         = route["share"]
        prices        = MODEL_PRICES[model_name]
        model_tokens  = tokens * share
        input_tokens  = model_tokens * ratio["input"]
        output_tokens = model_tokens * ratio["output"]
        cost = (
            (input_tokens  / 1_000_000) * prices["input"] +
            (output_tokens / 1_000_000) * prices["output"]
        )
        total_cost += cost
    return total_cost


def calc_cost_before_orgen(regular_count, dev_count, current_model="Claude Sonnet"):
    results = {}
    for user_type, count in [("regular_user", regular_count), ("developer", dev_count)]:
        if count == 0:
            results[user_type] = 0.0
            continue
        tokens        = calc_tokens_per_month(user_type, count)
        ratio         = INPUT_OUTPUT_RATIO[user_type]
        prices        = MODEL_PRICES[current_model]
        input_tokens  = tokens * ratio["input"]
        output_tokens = tokens * ratio["output"]
        cost = (
            (input_tokens  / 1_000_000) * prices["input"] +
            (output_tokens / 1_000_000) * prices["output"]
        )
        results[user_type] = cost
    results["total"] = results.get("regular_user", 0) + results.get("developer", 0)
    return results


def calc_cost_after_orgen(regular_count, dev_count):
    results = {}
    if regular_count > 0:
        tokens = calc_tokens_per_month("regular_user", regular_count)
        ratio  = INPUT_OUTPUT_RATIO["regular_user"]
        results["regular_user"] = calc_cost_for_routing(tokens, ORGEN_ROUTING["regular_users"], ratio)
    else:
        results["regular_user"] = 0.0

    if dev_count > 0:
        tokens = calc_tokens_per_month("developer", dev_count)
        ratio  = INPUT_OUTPUT_RATIO["developer"]
        results["developer"] = calc_cost_for_routing(tokens, ORGEN_ROUTING["developers"], ratio)
    else:
        results["developer"] = 0.0

    subtotal         = results["regular_user"] + results["developer"]
    results["fee"]   = PLATFORM_FEE
    results["total"] = subtotal + PLATFORM_FEE
    return results


def calc_manual_savings(line_items):
    total_before = 0.0
    total_saving = 0.0
    breakdown    = []
    for item in line_items:
        cost          = item["cost"]
        saving_pct    = MANUAL_SAVINGS.get(item["type"], 0.30)
        saving_amount = cost * saving_pct
        total_before += cost
        total_saving += saving_amount
        breakdown.append({
            **item,
            "saving_pct":    saving_pct,
            "saving_amount": saving_amount,
            "cost_after":    cost - saving_amount,
        })
    return {
        "breakdown":    breakdown,
        "total_before": total_before,
        "total_saving": total_saving,
        "total_after":  total_before - total_saving,
        "saving_pct":   total_saving / total_before if total_before > 0 else 0,
    }


def format_currency(amount):
    if amount >= 1_000_000:
        return f"${amount / 1_000_000:.1f}M"
    elif amount >= 1_000:
        return f"${amount:,.0f}"
    else:
        return f"${amount:.0f}"
