TYPES_EURO ={
    "Goles Metidos":int,
    "Goles Encajados":int,
    "Tiros a Puerta": int,
    "Penaltis Lanzados":int,
    "Posesion por Partido":int,
    "Entradas/Lances Ganados":int

}

def check_types(typ):
    def decorator_maker(fn):
        def wrapper(**kwargs):
            for k,v in kwargs.items():
                kwargs[k] = typ.get(k, str)(v)
            return fn (**kwargs)
        return wrapper
    return decorator_maker    

@check_types(TYPES_EURO)
def cast_types(**kwargs):
    return kwargs