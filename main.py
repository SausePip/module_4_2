def test_function():
    def inner_funcion():
        print('Я в области видимости функции test function')
    inner_funcion()

test_function()
inner_function() # При попытке вызвать данную функцию возникает ошибка, тк функция локальная, не объявлена глобально

