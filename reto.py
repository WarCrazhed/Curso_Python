def message_creator(text):
    answers = {
        'computadora': 'Con mi computadora puedo programar usando Python',
        'celular': 'En mi celular puedo aprender usando la app de Platzi',
        'cable': '¡Hay un cable en mi bota!'
    }

    if text in answers.keys(): 
        return answers[text]
    else: 
        return 'Artículo no encontrado'
      

text = 's'
response = message_creator(text)
print(response)