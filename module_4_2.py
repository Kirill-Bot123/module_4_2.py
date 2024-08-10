def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
iinner_function()   # естественно выдаст ошибку
# так как при поптыке вызвать функци inner_function она находилась внутри функции test_function
# соответственно вызвать ее можно только через функцию test_function
# потому что функция test_function находится в глобальном пространстве имен
# а iinner_function наоборот в локальном пространстве имен
