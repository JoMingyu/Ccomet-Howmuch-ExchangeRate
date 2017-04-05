# -*- coding: utf-8 -*-

# 계정
register_account_format = "INSERT INTO account(uuid, connected_sns, id, password) VALUES('%s', false, '%s', '%s')"
register_sns_account_format = "INSERT INTO account(uuid, connected_sns, google_id) VALUES ('%s', true, '%s')"
register_client_token_format = "INSERT INTO client_tokens(uuid, client_token)"

# 옵션
percentage_insert_format = "INSERT INTO options(id, src_nation, dst_nation, fall_percentage, rise_percentage, percentage_criteria) VALUES('%s', '%s', '%s', %f, %f, %f)"
percentage_update_format = "UPDATE options SET fall_percentage=%f, rise_percentage=%f, percentage_criteria=%f WHERE id='%s' AND src_nation='%s' AND dst_nation='%s'"

fixed_value_insert_format = "INSERT INTO options(id, src_nation, dst_nation, fixed_value_lower_limit, fixed_value_upper_limit) VALUES('%s', '%s', '%s', %f, %f)"
fixed_value_update_format = "UPDATE options SET fixed_value_lower_limit=%f, fixed_value_upper_limit=%f WHERE id='%s' AND src_nation='%s' AND dst_nation='%s'"

boolean_options_insert_format = "INSERT INTO options(id, src_nation, dst_nation, every_change, every_rise, every_fall) VALUES('%s', '%s', '%s', %s, %s, %s)"
boolean_options_update_format = "UPDATE options SET every_change=%s, every_rise=%s, every_fall=%s WHERE id='%s' AND src_nation='%s' AND dst_nation='%s'"

option_select_format = "SELECT * FROM options WHERE id='%s' AND src_nation='%s' AND dst_nation='%s'"

# 환율
exchange_rate_delete_format = "DELETE FROM current_exchange_rates WHERE src_nation='%s' AND dst_nation='%s'"
exchange_rate_insert_format = "INSERT INTO current_exchange_rates(src_nation, dst_nation, exchange_rate) VALUES('%s', '%s', %f)"
exchange_rate_select_format = "SELECT exchange_rate FROM current_exchange_rates WHERE src_nation='%s' AND dst_nation='%s'"
identical_code_select_format = "SELECT exchange_rate FROM current_exchange_rates WHERE src_nation='%s' AND dst_nation='=X'"

# 하루 단위 환율
daily_exchange_rate_insert_format = "INSERT INTO daily_exchange_rate("