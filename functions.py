def say_hello(person):
    print("hello " + person)

def fahr2celsius(fahr):
    celsius = (5 * (fahr -32)) / 9
    return celsius

print("Celsiuis: ", round(fahr2celsius(100),2))