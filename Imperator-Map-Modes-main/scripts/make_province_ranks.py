def get_metropolis(name, color):
	return """
{name} = {{
	rank_modifier = {{
		local_population_capacity = 30
		local_population_capacity_modifier = 0.1
		local_building_slot = 4
		local_pop_promotion_speed_modifier = 0.10
		local_migration_attraction = 2
		base_resources = 1
		local_state_trade_routes = 1
		local_nobles_desired_pop_ratio = 0.1
		local_citizen_desired_pop_ratio = 0.3
		local_freemen_desired_pop_ratio = 0.3
		local_slaves_desired_pop_ratio = 0.05
	}}
	color = {color}
	is_established_city = yes
	holy_site_treasure_slots = 3
}}""".format(color=color, name=name)

def get_city(name, color):
	return """
{name} = {{
	rank_modifier = {{
		local_population_capacity = 22 
		local_building_slot = 2
		local_nobles_desired_pop_ratio = 0.15
		local_citizen_desired_pop_ratio = 0.3
		local_freemen_desired_pop_ratio = 0.4
		local_slaves_desired_pop_ratio = 0.15
	}}
	color = {color}
	is_established_city = yes
	holy_site_treasure_slots = 2
}}""".format(color=color, name=name)

def get_settlement(name, color):
	return """
{name} = {{
	rank_modifier = {{
		local_citizen_desired_pop_ratio = 0.025
		local_population_capacity = 5
		local_migration_speed_modifier = -0.75
		local_output_modifier = -0.15
		local_pop_promotion_speed_modifier = -0.25
		local_goods_from_slaves = -5
		local_country_civilization_value = -5
		local_migration_attraction = -3
		local_ship_recruit_speed = -0.5
	}}
	color = {color}
	holy_site_treasure_slots = 1
}}""".format(color=color, name=name)


# ----------------------------------
# -  Print Citizen Province Ranks  -
# ----------------------------------

# color_v = 0
# for i in range(0, 21):
# 	if i == 0:
# 		color_v += 0.01
# 		color = "hsv {{ 0.44 0.9 {:.2f} }}".format(color_v) # Citizens color
# 		print(get_metropolis(f"city_metropolis_citizens_{i}", color))
# 		print(get_city(f"city_citizens_{i}", color))
# 		print(get_settlement(f"settlement_citizens_{i}", color))
# 	else:
# 		color_v += 0.02
# 		color = "hsv {{ 0.44 0.9 {:.2f} }}".format(color_v) # Citizens color
# 		print(get_metropolis(f"city_metropolis_citizens_{i}", color))
# 		print(get_city(f"city_citizens_{i}", color))
# 		print(get_settlement(f"settlement_citizens_{i}", color))
# for i in range(25, 55, 5):
# 	color_v += 0.1
# 	if i == 50:
# 		color_v -= 0.01
# 		color = "hsv {{ 0.44 0.9 {:.2f} }}".format(color_v) # Citizens color
# 		print(get_metropolis(f"city_metropolis_citizens_{i}", color))
# 		print(get_city(f"city_citizens_{i}", color))
# 		print(get_settlement(f"settlement_citizens_{i}", color))
# 	else:
# 		color = "hsv {{ 0.44 0.9 {:.2f} }}".format(color_v) # Citizens color
# 		print(get_metropolis(f"city_metropolis_citizens_{i}", color))
# 		print(get_city(f"city_citizens_{i}", color))
# 		print(get_settlement(f"settlement_citizens_{i}", color))

# ----------------------------------
# -  Print Freemen Province Ranks  -
# ----------------------------------

# color_v = 0
# for i in range(0, 21):
# 	if i == 0:
# 		color_v += 0.01
# 		color = "hsv {{ 0.08 0.9 {:.2f} }}".format(color_v) # Freemen color
# 		print(get_metropolis(f"city_metropolis_freemen_{i}", color))
# 		print(get_city(f"city_freemen_{i}", color))
# 		print(get_settlement(f"settlement_freemen_{i}", color))
# 	else:
# 		color_v += 0.02
# 		color = "hsv {{ 0.08 0.9 {:.2f} }}".format(color_v) # Freemen color
# 		print(get_metropolis(f"city_metropolis_freemen_{i}", color))
# 		print(get_city(f"city_freemen_{i}", color))
# 		print(get_settlement(f"settlement_freemen_{i}", color))
# for i in range(25, 55, 5):
# 	color_v += 0.1
# 	if i == 50:
# 		color_v -= 0.01
# 		color = "hsv {{ 0.08 0.9 {:.2f} }}".format(color_v) # Freemen color
# 		print(get_metropolis(f"city_metropolis_freemen_{i}", color))
# 		print(get_city(f"city_freemen_{i}", color))
# 		print(get_settlement(f"settlement_freemen_{i}", color))
# 	else:
# 		color = "hsv {{ 0.08 0.9 {:.2f} }}".format(color_v) # Freemen color
# 		print(get_metropolis(f"city_metropolis_freemen_{i}", color))
# 		print(get_city(f"city_freemen_{i}", color))
# 		print(get_settlement(f"settlement_freemen_{i}", color))


# ----------------------------------
# -  Print Slaves Province Ranks   -
# ----------------------------------

# color_v = 0
# for i in range(0, 21):
# 	if i == 0:
# 		color_v += 0.01
# 		color = "hsv {{ 0.14 0.9 {:.2f} }}".format(color_v) # Slaves color
# 		print(get_metropolis(f"city_metropolis_slaves_{i}", color))
# 		print(get_city(f"city_slaves_{i}", color))
# 		print(get_settlement(f"settlement_slaves_{i}", color))
# 	else:
# 		color_v += 0.02
# 		color = "hsv {{ 0.14 0.9 {:.2f} }}".format(color_v) # Slaves color
# 		print(get_metropolis(f"city_metropolis_slaves_{i}", color))
# 		print(get_city(f"city_slaves_{i}", color))
# 		print(get_settlement(f"settlement_slaves_{i}", color))
# for i in range(25, 55, 5):
# 	color_v += 0.1
# 	if i == 50:
# 		color_v -= 0.01
# 		color = "hsv {{ 0.14 0.9 {:.2f} }}".format(color_v) # Slaves color
# 		print(get_metropolis(f"city_metropolis_slaves_{i}", color))
# 		print(get_city(f"city_slaves_{i}", color))
# 		print(get_settlement(f"settlement_slaves_{i}", color))
# 	else:
# 		color = "hsv {{ 0.14 0.9 {:.2f} }}".format(color_v) # Slaves color
# 		print(get_metropolis(f"city_metropolis_slaves_{i}", color))
# 		print(get_city(f"city_slaves_{i}", color))
# 		print(get_settlement(f"settlement_slaves_{i}", color))

# ----------------------------------
# -  Print Nobles Province Ranks   -
# ----------------------------------

# color_v = 0
# for i in range(0, 21):
# 	if i == 0:
# 		color_v += 0.01
# 		color = "hsv {{ 0.8 0.9 {:.2f} }}".format(color_v) # Nobles color
# 		print(get_metropolis(f"city_metropolis_nobles_{i}", color))
# 		print(get_city(f"city_nobles_{i}", color))
# 		print(get_settlement(f"settlement_nobles_{i}", color))
# 	else:
# 		color_v += 0.02
# 		color = "hsv {{ 0.8 0.9 {:.2f} }}".format(color_v) # Nobles color
# 		print(get_metropolis(f"city_metropolis_nobles_{i}", color))
# 		print(get_city(f"city_nobles_{i}", color))
# 		print(get_settlement(f"settlement_nobles_{i}", color))
# for i in range(25, 55, 5):
# 	color_v += 0.1
# 	if i == 50:
# 		color_v -= 0.01
# 		color = "hsv {{ 0.8 0.9 {:.2f} }}".format(color_v) # Nobles color
# 		print(get_metropolis(f"city_metropolis_nobles_{i}", color))
# 		print(get_city(f"city_nobles_{i}", color))
# 		print(get_settlement(f"settlement_nobles_{i}", color))
# 	else:
# 		color = "hsv {{ 0.8 0.9 {:.2f} }}".format(color_v) # Nobles color
# 		print(get_metropolis(f"city_metropolis_nobles_{i}", color))
# 		print(get_city(f"city_nobles_{i}", color))
# 		print(get_settlement(f"settlement_nobles_{i}", color))

# ----------------------------------
# - Print Tribesmen Province Ranks -
# ----------------------------------

# color_v = 0
# for i in range(0, 21):
# 	if i == 0:
# 		color_v += 0.01
# 		color = "hsv {{ 0.24 0.9 {:.2f} }}".format(color_v) # Tribesmen color
# 		print(get_metropolis(f"city_metropolis_tribesmen_{i}", color))
# 		print(get_city(f"city_tribesmen_{i}", color))
# 		print(get_settlement(f"settlement_tribesmen_{i}", color))
# 	else:
# 		color_v += 0.02
# 		color = "hsv {{ 0.24 0.9 {:.2f} }}".format(color_v) # Tribesmen color
# 		print(get_metropolis(f"city_metropolis_tribesmen_{i}", color))
# 		print(get_city(f"city_tribesmen_{i}", color))
# 		print(get_settlement(f"settlement_tribesmen_{i}", color))
# for i in range(25, 55, 5):
# 	color_v += 0.1
# 	if i == 50:
# 		color_v -= 0.01
# 		color = "hsv {{ 0.24 0.9 {:.2f} }}".format(color_v) # Tribesmen color
# 		print(get_metropolis(f"city_metropolis_tribesmen_{i}", color))
# 		print(get_city(f"city_tribesmen_{i}", color))
# 		print(get_settlement(f"settlement_tribesmen_{i}", color))
# 	else:
# 		color = "hsv {{ 0.24 0.9 {:.2f} }}".format(color_v) # Tribesmen color
# 		print(get_metropolis(f"city_metropolis_tribesmen_{i}", color))
# 		print(get_city(f"city_tribesmen_{i}", color))
# 		print(get_settlement(f"settlement_tribesmen_{i}", color))

# -----------------------------------
# - Print Technology Province Ranks -
# -----------------------------------

# color_v = 0
# for i in range(0, 21):
# 	if i == 0:
# 		color_v += 0.01
# 		color = "hsv {{ 0.0 0.9 {:.2f} }}".format(color_v) # Tech color
# 		print(get_metropolis(f"city_metropolis_tech_{i}", color))
# 		print(get_city(f"city_tech_{i}", color))
# 		print(get_settlement(f"settlement_tech_{i}", color))
# 	elif i == 20:
# 		color_v += 0.03
# 		color = "hsv {{ 0.0 0.9 {:.2f} }}".format(color_v) # Tech color
# 		print(get_metropolis(f"city_metropolis_tech_{i}", color))
# 		print(get_city(f"city_tech_{i}", color))
# 		print(get_settlement(f"settlement_tech_{i}", color))
# 	else:
# 		color_v += 0.05
# 		color = "hsv {{ 0.0 0.9 {:.2f} }}".format(color_v) # Tech color
# 		print(get_metropolis(f"city_metropolis_tech_{i}", color))
# 		print(get_city(f"city_tech_{i}", color))
# 		print(get_settlement(f"settlement_tech_{i}", color))

for i in range(0,21):
	string = """
	if = {{
		limit = {{
			military_tech = {i}
		}}
		every_owned_province = {{
			limit = {{
				has_province_rank = settlement
			}}
			set_variable = {{
				name = p_rank
				value = 1
			}}
			set_city_status = settlement_tech_{i}
		}}
		every_owned_province = {{
			limit = {{
				has_province_rank = city
			}}
			set_variable = {{
				name = p_rank
				value = 2
			}}
			set_city_status = city_tech_{i}
		}}
		every_owned_province = {{
			limit = {{
				has_province_rank = city_metropolis
			}}
			set_variable = {{
				name = p_rank
				value = 3
			}}
			set_city_status = city_metropolis_tech_{i}
		}}
	}}""".format(i=i)
	print(string)