import par, tet, bal

def list_options():
    return ["Параллелепипед", "Тетраэдр", "Шар"]

def select(x: str):
    global selected
    match x:
        case "Параллелепипед":
            selected = par
        case "Тетраэдр":
            selected = tet
        case "Шар":
            selected = bal
        case _:
            return "Нет такого: " + x
    global volume = selected.volume
    global surface = selected.surface

select('Параллелепипед')

material_list = {'сталь': 7850, 'стекло': 2500, 'бетон': 2000}

def mass(a,b,c,m):
    try: mm = material_list[m]
    except: return 'Не знаю материала "{m}"'
    return selected.volume(a,b,c)*mm
