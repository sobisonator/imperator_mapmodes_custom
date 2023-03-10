def print_mapmode_statement(i,r):
    loc = """         else_if = {{
				limit = {{ WEALTH_pop_score < {r} }}
				set_city_status = mapmode_generic_count_{i}
			}}""".format(i=i,r=r)
    print(loc)

i = 1
r = 1
while i < 125:
    print_mapmode_statement(i,int(r))
    if r >= 17:
        r = r * 1.035
    elif r < 17:
        r = r + 1
    i = i+1
