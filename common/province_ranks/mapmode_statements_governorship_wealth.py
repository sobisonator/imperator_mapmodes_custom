def print_mapmode_statement(i,r):
    loc = """         else_if = {{
				limit = {{ WEALTH_governorship_total < {r} }}
				run_script_in_every_governorship_province = {{
					script = "set_city_status = mapmode_generic_count_{i}"
				}}
			}}""".format(i=i,r=r)
    print(loc)

i = 1
r = 1
while i < 125:
    print_mapmode_statement(i,int(r))
    if r >= 16:
        r = r * 1.04
    elif r < 16:
        r = r + 1
    i = i+1
