def sozluk_sirala(sozluk, anahtar=True):
    if anahtar:
        return dict(sorted(sozluk.items()))
    else:
        return dict(sorted(sozluk.items(), key=lambda item: item[1]))
    
sozluk ={"c": 3, "a": 1, "b": 2}
print(sozluk_sirala(sozluk)) # {'a': 1, 'b': 2, 'c': 3}
print(sozluk_sirala(sozluk, anahtar=False)) # {'a': 1, 'b': 2, 'c': 3}