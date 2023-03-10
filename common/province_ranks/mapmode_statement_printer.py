def print_mapmode_statement(i,r,g):
    loc = """mapmode_generic_count_{i} = {{
	rank_modifier = {{}}

	color = rgb {{ {r} {g} 0}}
	is_established_city = no
	holy_site_treasure_slots 3
}}""".format(i=i,r=r, g=g)
    print(loc)

for i in range(1,125):
    print_mapmode_statement(i,2*(125-i), 2*i)
