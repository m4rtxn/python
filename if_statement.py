is_enabled = False
is_active= True
is_new=False

if is_enabled and is_active:
    print("System is active and running")
#Si la condición no se cumple puede evaluar una nueva
elif is_new :
        print("System is not new")
# else if sirve para evaluar una nueva condición en caso de que la primera no se cumpla
# en cambio el else solo ejecuta la acción por defecto en caso de que nada se cumpla
else:
    print("system is not running")