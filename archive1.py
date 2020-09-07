diccionario = dict(nombres = ['Miguel', 'Bernardo', 'Rafael', 'Gian'], apellidos = ['Buonarrotti', 'Rossellino', 'Sanzio', 'Bernini'], cursos = ['programacion', 'estadistica'], notas_programacion = [7.0, 5.6, 6.5, 6.1], notas_estadistica= [5.8, 6.7, 5.9, 6.2])                                                                         
diccionario.pop('notas_estadistica')                                                                                                                                
[5.8, 6.7, 5.9, 6.2]                                                                                                                                                   
diccionario['notas_fisica'] = [5.1, 6.2, 5.9, 6.0]                                                                                                                 
print(diccionario['nombres'][0], diccionario['apellidos'][0], diccionario['notas_programacion'][0], diccionario['notas_fisica'][0]) 
