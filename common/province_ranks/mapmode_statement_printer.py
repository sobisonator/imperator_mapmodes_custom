def print_generic_count_mapmode_statement(province_rank,rank_modifier,
                                          city_status,
                                          i,
                                          h,
                                          s,
                                          v):
    loc = """mapmode_generic_count_{province_rank}_{i} = {{
	{rank_modifier}

	color = hsv {{ {h} {s} {v} }}
	is_established_city = {city_status}
	holy_site_treasure_slots = 3
}}""".format(province_rank=province_rank,
             rank_modifier=rank_modifier,
             city_status=city_status,
             i=i,h=h, s=s, v=v)
    print(loc)

province_ranks = ["settlement","city","city_metropolis"]

def rgb_colour_scale_black_to_green(i):
    return(0,0,2*i)
def rgb_colour_scale_yellow_to_red(i):
    return(i,2*(125-i), 2*(125-i), 2*i)
def hsv_colour_scale_black_to_green(i):
    return()

for province_rank in province_ranks:
    if province_rank == "settlement":
        rank_modifier = """	rank_modifier = {
		local_population_capacity = 5
		local_migration_speed_modifier = -0.75
		local_migration_attraction = -3
		local_pop_promotion_speed_modifier = -0.25
		local_ship_recruit_speed = -0.5
	}"""
        for i in range(1,125):  
            print_generic_count_mapmode_statement(province_rank,
                                    rank_modifier,
                                    "no",i,
                                    0.7,(i/125),(i/125))
            
    elif province_rank == "city":
        rank_modifier = """	rank_modifier = {
		local_building_slot = 10 # Same as settlement
		local_population_capacity = 22 
		base_resources = 1
	}"""
        for i in range(1,125):  
            print_generic_count_mapmode_statement(province_rank,
                                    rank_modifier,
                                    "yes",i,
                                    0.7,(i/125),(i/125))
            
    elif province_rank == "city_metropolis":
        rank_modifier = """	rank_modifier = {
		local_building_slot = 10 # Same as settlement
		local_population_capacity = 30
		local_population_capacity_modifier = 0.1
		local_pop_promotion_speed_modifier = 0.10
		local_migration_attraction = 2
	}"""
        for i in range(1,125):  
            print_generic_count_mapmode_statement(province_rank,
                                    rank_modifier,
                                    "yes",i,
                                    0.7,(i/125),(i/125))
