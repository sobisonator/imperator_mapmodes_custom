def print_mapmode_statement(i,r):
    loc = """         else_if = {{
				limit = {{ WEALTH_governorship_per_capita < {r} }}
				run_script_in_every_governorship_province = {{
					script = "set_city_status = mapmode_generic_count_{i}"
				}}
			}}""".format(i=i,r=r)
    print(loc)

i = 1
r = 0.01
while i < 125:
    print_mapmode_statement(i,round(r,3))
    if r >= 0.02:
        r = r * 1.03
    elif r < 0.02:
        r = r + 0.001
    i = i+1
